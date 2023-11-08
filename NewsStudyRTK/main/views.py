from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def index(request):
    value = -10
    n1 = News('news1', 'txt1', '01.07.2023')
    n2 = News('news2', 'txt2', '01.07.2023')
    l = [n1, n2]
    context = {'title': 'Main page',
               'header1': 'Header of page',
               'value': value,
               'numbers': l,
               }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('<h1> About us </h1>')
def contacts(request):
    return HttpResponse('<h1> Contacts </h1>')

def sidebar(request):
    return render(request, 'main/sidebar.html')