from django.http import HttpResponse
from django.shortcuts import render

def HomeRender(request):
    return HttpResponse('<h1>Авторизация</h1>')
