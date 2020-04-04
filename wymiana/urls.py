from django.urls import path
from wymiana import views
from .views import wymiana, WymianaCreateView, WymianaUpdateView, WymianaDeleteView,\
                   KomentarzUpdateView, KomentarzDeleteView, wymiana_lista, dodaj_plik

urlpatterns = [
    path('', views.glowna, name='glowna'),
    path('wymiana/<int:pk>', wymiana, name='wymiana_szczegoly'),
    path('wymiana/<int:pk>/galeria', dodaj_plik, name='galeria'),
    path('wymiana/nowa', WymianaCreateView.as_view(), name='wymiana_utworz'),
    path('wymiana/lista', wymiana_lista, name='wymiana_lista'),
    path('wymiana/<int:pk>/aktualizuj', WymianaUpdateView.as_view(), name='wymiana_aktualizuj'),
    path('wymiana/<int:pk>/usun', WymianaDeleteView.as_view(), name='wymiana_usun'),
    path('komantarz/<int:pk>/aktualizuj', KomentarzUpdateView.as_view(), name='komentarz_aktualizuj'),
    path('komantarz/<int:pk>/usun', KomentarzDeleteView.as_view(), name='komentarz_usun'),
]
