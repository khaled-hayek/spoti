# Generated by Django 4.1.4 on 2022-12-11 18:51

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('popularity', models.IntegerField()),
                ('type', models.CharField(max_length=255)),
                ('uri', models.CharField(max_length=255)),
                ('href', models.CharField(max_length=255)),
                ('genres', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('url', models.CharField(max_length=255)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('href', models.CharField(max_length=255)),
                ('total', models.IntegerField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.artist')),
            ],
        ),
        migrations.CreateModel(
            name='ExternalUrls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.artist')),
            ],
        ),
    ]