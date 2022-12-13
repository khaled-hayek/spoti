from rest_framework import serializers
from artist.models import Artist, Images, Followers, ExternalUrls


class ExternalUrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalUrls
        exclude = ["id", "artist"]



class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        exclude = ["id", "artist"]


class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Followers
        exclude = ["id", "artist"]


class ArtistSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, allow_null=True)
    followers = FollowersSerializer()
    external_urls = ExternalUrlsSerializer()
    class Meta:
        model = Artist
        fields = '__all__'
        depth = 5
