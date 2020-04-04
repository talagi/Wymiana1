from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from konta.forms import ProfilForm, UzytkownikForm
from konta.models import Profil


@login_required
def wyloguj(request):
    logout(request)
    return HttpResponseRedirect(reverse('glowna'))


def rejestracja(request):
    registered = False
    if request.method == 'POST':
        print(request.POST)
        formularz_uzytkownika = UzytkownikForm(request.POST)
        formularz_profilu = ProfilForm(request.POST, request.FILES)
        if formularz_uzytkownika.is_valid() and formularz_profilu.is_valid():
            uzytkownik = formularz_uzytkownika.save()
            uzytkownik.save()
            profil = formularz_profilu.save(commit=False)
            profil.user = uzytkownik
            profil.save()
            registered = True
        else:
            print(formularz_uzytkownika.errors, formularz_profilu.errors)
    else:
        formularz_uzytkownika = UzytkownikForm()
        formularz_profilu = ProfilForm()
    return render(request, 'konta/rejestracja.html',
                  {'formularz_uzytkownika': formularz_uzytkownika,
                   'formularz_profilu': formularz_profilu,
                   'registered': registered})


def logowanie(request):
    if request.method == 'POST':
        nazwa = request.POST.get('username')
        haslo = request.POST.get('password')
        uzytkownik = authenticate(username=nazwa, password=haslo)
        if uzytkownik:
            if uzytkownik.is_active:
                login(request, uzytkownik)
                return HttpResponseRedirect(reverse('glowna'))
            else:
                return HttpResponse("Twoje konto jest niekatywne.")
        else:
            return HttpResponse("Złe dane logowania")
    else:
        return render(request, 'konta/logowanie.html')


@login_required()
def profil(request, pk):
    if request.method == 'POST':
        instance = get_object_or_404(Profil, user=pk)
        formularz_profilu = ProfilForm(request.POST or None, request.FILES, instance=instance)
        if formularz_profilu.is_valid():
            formularz_profilu.save()
        return redirect('profil', pk=pk)
    else:
        profil = Profil.objects.get(user=pk)
        formularz_profilu = ProfilForm()
        context = {
            'formularz_profilu': formularz_profilu,
            'profil': profil,
        }
        return render(request, 'konta/profil.html', context)
