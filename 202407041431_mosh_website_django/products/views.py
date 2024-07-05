from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def new(request):
    return HttpResponse('New product.')

def create(request):
    return HttpResponse('Create page')

def update(request):
    return HttpResponse('Update page')
