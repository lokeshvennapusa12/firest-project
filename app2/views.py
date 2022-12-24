from django.shortcuts import render
from django.http import HttpResponse

def firest(request):
    return HttpResponse('<h1>This is My Firest Project</h1>')

def second(request):
    return HttpResponse('<h1>This is My Second Project</h1>')

