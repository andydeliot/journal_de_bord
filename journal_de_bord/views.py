from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """ Affiche toutes mes journées de mon journal de bord. """
    return HttpResponse("<h1>Hello, world !</h1>")


