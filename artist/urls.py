
from django.urls import path

import artist
from . import views


urlpatterns = [
    path('v1/artist', artist.views.ArtistList.as_view()),
    path('v1/artist/<str:pk>', artist.views.ArtistDetail.as_view()),

]