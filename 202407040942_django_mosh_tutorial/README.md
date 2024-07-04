# Mosh Django course

- [Youtube vídeo](https://www.youtube.com/watch?v=rHux0gMZ3Eg)

- To start a project run `django-admin startproject`.

- The `storefront/manage.py` file could run the server as in `django-admin runserver` command.

- "Ctrl+`" to toggle the vc code terminal.

- The `storefornt/storefront/settings.py` we delited the `django.contrib.sessions` in the `INSTALLED_APPS` list. To mosh this is not used anymore.

- To start a new app run `python storefront/manage.py startapp playground` been playground here the name of our new app. After app creation we need to add it (`playground`) in `INSTALLED_APPS` list (`storefornt/storefront/settings.py` file).

- As I understood the `views.py` module inside the app's folder (`playground` until here) acts like a `controller` in `rails`. So we:
  - Built a `say_hello` function there (`views.py`)
  - Included it on a new file called `playground/urls.py` through the `urlpatterns` list (`URLConf`).
  - Included the `path('playgrond/', include('playgrond.urls'))` at the `playground/urls.py` (`urlpatterns`) folder in the `storefront/urls.py` file. Need to import the include module (`from django.urls import include`).

- Always end a route with `/`.
