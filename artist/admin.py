from django.contrib import admin

# Register your models here.
from artist.models import Artist, Followers, Images, ExternalUrls


class ExternalUrlsInLine(admin.TabularInline):
    model = ExternalUrls
    extra = 0
    show_change_link = False
    classes = ['collapse']

class FollowesInLine(admin.TabularInline):
    model = Followers
    extra = 0
    show_change_link = False
    classes = ['collapse']


class ImagesInLine(admin.StackedInline):
    model = Images
    extra = 0
    show_change_link = False
    classes = ['collapse']


class ArtistAdmin(admin.ModelAdmin):
    list_display = ["name", "popularity", "type"]
    search_fields = ["name"]
    inlines = [ExternalUrlsInLine, FollowesInLine, ImagesInLine]
    list_filter = ["type"]

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Followers)
admin.site.register(Images)
admin.site.register(ExternalUrls)
