# Generated by Django 2.2.10 on 2020-04-03 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konta', '0003_auto_20200403_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='zdjecie',
            field=models.ImageField(default='domyslne.png', upload_to='zdjecia/'),
        ),
    ]
