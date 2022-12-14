# Generated by Django 4.0.4 on 2022-12-13 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0004_alter_images_artist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='externalurls',
            old_name='name',
            new_name='spotify',
        ),
        migrations.RemoveField(
            model_name='externalurls',
            name='value',
        ),
        migrations.AlterField(
            model_name='externalurls',
            name='artist',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='external_urls', to='artist.artist'),
        ),
    ]
