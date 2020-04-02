# Generated by Django 2.2.10 on 2020-04-02 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('klasa', models.CharField(choices=[('1A', '1A'), ('2A', '2A'), ('3A', '3A')], max_length=4)),
                ('zdjecie', models.ImageField(default='domyslne.png', upload_to='zdjecia')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]