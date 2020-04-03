from django.urls import path
from wymiana import views


urlpatterns = [
    path('', views.glowna, name='glowna'),
]
