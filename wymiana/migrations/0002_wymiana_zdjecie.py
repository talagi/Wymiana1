# Generated by Django 2.2.10 on 2020-04-03 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wymiana', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wymiana',
            name='zdjecie',
            field=models.ImageField(default='domyslne.png', upload_to='wymiany/'),
        ),
    ]
