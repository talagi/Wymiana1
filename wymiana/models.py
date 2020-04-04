from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Wymiana(models.Model):
    tytul = models.CharField(max_length=80)
    tresc = models.TextField()
    data = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    zdjecie = models.ImageField(upload_to='wymiany/', default='produkt.png')

    class Meta:
        verbose_name_plural = "Wymiany"

    def __str__(self):
        return self.tytul + '_' + self.autor.username

    def get_absolute_url(self):
        return reverse('wymiana_szczegoly', kwargs={'pk': self.pk})


class WymianaPlik(models.Model):
    plik = models.FileField(upload_to="pliki")
    wymiana = models.ForeignKey(Wymiana, on_delete=models.CASCADE, related_name='plik')


class Komentarz(models.Model):
    wymiana = models.ForeignKey(Wymiana, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, max_length=200)
    tresc = models.TextField()
    data = models.DateTimeField(default=timezone.now, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Komentarze"

    def __str__(self):
        return self.tresc

    def get_absolute_url(self):
        return reverse('komentarz_utworz', kwargs={'pk': self.pk})
