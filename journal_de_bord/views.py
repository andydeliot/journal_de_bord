from django.shortcuts import render
from django.http import HttpResponse

from .models import Journee

def home(request):
    """ Affiche toutes mes journées de mon journal de bord. """
    journees = Journee.objects.all().order_by("-jour")
    print(locals())
    return render(request, "journal_de_bord/home.html", locals())


