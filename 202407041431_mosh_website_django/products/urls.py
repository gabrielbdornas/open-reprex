from django.urls import path
from . import views

# /products -> root of the site
urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('update/', views.update),
]
