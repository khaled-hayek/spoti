
import requests
from django.core.management.base import BaseCommand, CommandError

from artist.models import Artist, Followers, Images, ExternalUrls

# artists_id = ["5lpH0xAS4fVfLkACg9DAuM"]

artists_id =  ["4iHNK0tOyZPYnBU7nGAgpQ" , "5lpH0xAS4fVfLkACg9DAuM" , "0wi4yTYlGtEnbGo4ltZTib" , "1GxkXlMwML1oSg5eLPiAz3" , "38EmEgXkgK51MT2tPY0EoC" ,
               "4cPHsZM98sKzmV26wlwD2W" , "5KEG7G8LDYlHgFDqZyEEs2" , "7K78lVZ8XzkjfRSI7570FF" , "49e4v89VmlDcFCMyDv9wQ9" , "2apYMRrg5FxN4go0pfsCvf"]

class Command(BaseCommand):
    help = 'Fetch artists and store them to database'

    def add_arguments(self, parser):
        parser.add_argument('token',  type=str)

    def handle(self, *args, **options):
        token = options['token']
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}

        for artist in artists_id:
            url = 'https://api.spotify.com/v1/artists/{}'.format(artist)

            req = requests.get(url, headers=headers)
            print(req)
            if req.ok:
                print(req.status_code)
                # get data
                id = req.json()["id"]
                external_urls = req.json()["external_urls"]
                followers = req.json()["followers"]
                genres = req.json()["genres"]
                href = req.json()["href"]
                images = req.json()["images"]
                name = req.json()["name"]
                popularity = req.json()["popularity"]
                type = req.json()["type"]
                uri = req.json()["uri"]

                # create artist and related objects
                artist, created = Artist.objects.get_or_create(id=id , name=name , popularity=popularity, type=type , uri=uri, href=href, genres=genres)

                if created:
                    if followers:
                        Followers.objects.create(href=followers['href'], total=followers['total'], artist=artist)
                    if images:
                        for image in images:
                            Images.objects.create(height=image["height"] , width=image["width"], url=image["url"] ,artist=artist)
                    if external_urls:
                        ExternalUrls.objects.create(spotify=external_urls['spotify'], artist=artist)