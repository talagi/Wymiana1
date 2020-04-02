from django.db import models
from django.contrib.auth.models import User
from PIL import Image

KLASY = (
    ('1A', '1A'),
    ('2A', '2A'),
    ('3A', '3A'),
)


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    klasa = models.CharField(choices=KLASY, max_length=4)
    zdjecie = models.ImageField(upload_to='zdjecia', default='domyslne.png')

    def __str__(self):
      return self.user.username