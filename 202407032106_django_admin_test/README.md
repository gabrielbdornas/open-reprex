# comandos

django-admin startproject core .

python manage.py startapp blog

Add this two apps to `core/settings.py`, `INSTALLED_APPS` property.

python manage.py runserver

python manage.py migrate

python manage.py createsuperuser

depois de criar uma classe (model): `python manage.py makemigrations`

para migrar: `python manage.py migrate`
