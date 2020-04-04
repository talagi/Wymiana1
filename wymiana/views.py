from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, \
    UpdateView, DeleteView

from .forms import KomentarzForm, PlikForm
from .models import Wymiana, Komentarz, WymianaPlik


def glowna(request):
    return render(request, 'wymiana/glowna.html')


def wymiana_lista(request):
    wymiany = Wymiana.objects.all().order_by('-data')
    return render(request, 'wymiana/wymiana_lista.html', {'wymiany': wymiany})


def wymiana(request, pk):
    if request.method == 'POST':
        wymiana = get_object_or_404(Wymiana, pk=pk)
        formularz = KomentarzForm(request.POST or None)
        if formularz.is_valid():
            formularz.instance.wymiana = wymiana
            formularz.instance.autor = request.user
            formularz.save()
        return redirect('wymiana_szczegoly', pk)
    else:
        wymiana = Wymiana.objects.get(pk=pk)
        komentarze = Komentarz.objects.filter(wymiana=pk)
        form = KomentarzForm()
        context = {
            'wymiana': wymiana,
            'komentarze': komentarze,
            'form': form,
        }

        return render(request, 'wymiana/wymiana_detail.html', context)


def dodaj_plik(request, pk):
    if request.method == 'POST':
        formularz = PlikForm(request.POST, request.FILES)
        pliki = request.FILES.getlist('plik')
        wymiana = Wymiana.objects.get(pk=pk)
        if formularz.is_valid():
            for p in pliki:
                plik = WymianaPlik(plik=p, wymiana=wymiana)
                plik.save()
        return redirect('galeria', pk)
    else:
        autor = Wymiana.objects.get(pk=pk).autor
        formularz = PlikForm()
        pliki = WymianaPlik.objects.filter(wymiana_id=pk)
        context = {
            'formularz': formularz,
            'pliki': pliki,
            'autor': autor,
        }
    return render(request, 'wymiana/wymiana_pliki.html', context)


class WymianaCreateView(LoginRequiredMixin, CreateView):
    model = Wymiana
    fields = ['tytul', 'tresc', 'zdjecie']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class WymianaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Wymiana
    fields = ['tytul', 'tresc']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Wymiana = self.get_object()
        if self.request.user == Wymiana.autor:
            return True
        return False


class WymianaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Wymiana
    success_url = '/'

    def test_func(self):
        Wymiana = self.get_object()
        if self.request.user == Wymiana.autor:
            return True
        return False


class KomentarzUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Komentarz
    fields = ['tresc']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        komentarz = self.get_object()
        if self.request.user == komentarz.autor:
            return True
        return False

    def get_success_url(self, **kwargs):
        pk = self.object.wymiana.pk
        return reverse('wymiana_szczegoly', kwargs={'pk': pk})


class KomentarzDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Komentarz

    def get_success_url(self, **kwargs):
        pk = self.object.wymiana.id
        return reverse('wymiana_szczegoly', kwargs={'pk': pk})

    def test_func(self):
        komentarz = self.get_object()
        if self.request.user == komentarz.autor:
            return True
        return False
