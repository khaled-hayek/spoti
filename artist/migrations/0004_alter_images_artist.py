# Generated by Django 4.0.4 on 2022-12-13 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0003_alter_followers_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='artist.artist'),
        ),
    ]
