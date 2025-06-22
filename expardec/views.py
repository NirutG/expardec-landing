from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def index_es(request):
    return render(request, 'index_es.html')

def about_es(request):
    return render(request, 'about_es.html')

def contact_es(request):
    return render(request, 'contact_es.html')