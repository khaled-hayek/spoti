from django.db import models
from django.contrib.postgres.fields import ArrayField


class Artist(models.Model):
    id = models.CharField(primary_key=True, max_length=255, blank=False, null=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    popularity = models.IntegerField()
    type = models.CharField(max_length=255)
    uri = models.CharField(max_length=255)
    href = models.CharField(max_length=255)
    genres = ArrayField(models.CharField(max_length=255))

    def __str__(self):
        return self.name


class Followers(models.Model):
    href = models.CharField(max_length=255, null=True, blank=True)
    total = models.IntegerField()
    artist = models.OneToOneField(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.artist.name + "'s followers"

    class Meta:
        verbose_name = 'Followers'
        verbose_name_plural = "Followers"


class ExternalUrls(models.Model):
    spotify = models.CharField(max_length=255)
    artist = models.OneToOneField(Artist, related_name='external_urls', on_delete=models.CASCADE)

    def __str__(self):
        return self.spotify

    class Meta:
        verbose_name = 'External Urls'
        verbose_name_plural = "External Urls"


class Images(models.Model):
    height = models.IntegerField()
    width = models.IntegerField()
    url = models.CharField(max_length=255)
    artist = artist = models.ForeignKey(Artist, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.artist.name + "'s image"


    class Meta:
        verbose_name = 'Images'
        verbose_name_plural = "Images"