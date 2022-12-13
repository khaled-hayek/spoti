from django.shortcuts import render

from rest_framework import generics

from artist.models import Artist
from artist.serializers import ArtistSerializer


class ArtistList(generics.CreateAPIView, generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
