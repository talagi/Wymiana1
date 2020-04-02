from django.shortcuts import render
from konta.forms import ProfilForm, UzytkownikForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def glowna(request):
    return render(request, 'konta/glowna.html')



@login_required
def wyloguj(request):
    logout(request)
    return HttpResponseRedirect(reverse('glowna'))


def rejestracja(request):
    registered = False
    if request.method == 'POST':
        user_form = UzytkownikForm(data=request.POST)
        profile_form = ProfilForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UzytkownikForm()
        profile_form = ProfilForm()
    return render(request,'konta/rejestracja.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


def logowanie(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('glowna'))
            else:
                return HttpResponse("Twoje konto jest niekatywne.")
        else:
            return HttpResponse("Złe dane logowania")
    else:
        return render(request, 'konta/logowanie.html')