# django-wcl-skel

Our basic Django skel for webservices

Pre-reqs:

* [cookiecutter](https://github.com/audreyr/cookiecutter)
* [postgresql](http://www.postgresql.org)

Run:

```sh
$ cookiecutter https://github.com/westerncapelabs/django-wcl-skel
```

Setup and test:

```sh
$ cd newrepo
$ psql postgres -c "CREATE DATABASE newrepo"
$ pyenv virtualenv 3.4.2 newrepo
$ pyenv shell newrepo
(newrepo) $ pip install -r requirements.txt
(newrepo) $ pip install -r requirements-dev.txt
(newrepo) $ ./manage.py makemigrations
(newrepo) $ ./manage.py migrate
```

Run
```sh
(newrepo) $ export DEBUG=True
(newrepo) $ ./manage.py createsuperuser
(newrepo) $ ./manage.py runserver
```
