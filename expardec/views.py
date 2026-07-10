from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def partnerships(request):
    return render(request, 'partnerships.html')

def news_asocam(request):
    return render(request, 'news_asocam.html')

def contact(request):
    return render(request, 'contact.html')

def index_es(request):
    return render(request, 'index_es.html')

def about_es(request):
    return render(request, 'about_es.html')

def partnerships_es(request):
    return render(request, 'partnerships_es.html')

def news_asocam_es(request):
    return render(request, 'news_asocam_es.html')

def contact_es(request):
    return render(request, 'contact_es.html')