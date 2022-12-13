# spoti

1- Install PostgreSQL.

2- Clone project and create virtual env.

3- Install dep. 
>pip install -r requirements.txt

4- Run migrations
> python manage.py migrate

5- Run the server 
> python manage.py runserver


To login to admin page:

1- Create superuser
> python manage.py createsuperuser

2- Visit
>http://localhost:8000/admin


To fetch data:
Run managment command
> python manage.py fetch **spotify_token**

Note: **spotify_token** is a string can be gotten from
>https://developer.spotify.com/console/get-artist/
