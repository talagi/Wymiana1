from django.urls import path
from konta import views


urlpatterns = [
    path('', views.glowna, name='glowna'),
    path('rejestracja/', views.rejestracja, name='rejestracja'),
    path('logowanie', views.logowanie, name='logowanie'),
    path('wylogowanie', views.wyloguj, name='wylogowanie'),
]