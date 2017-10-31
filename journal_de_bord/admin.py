from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from .models import Journee, Souvenir, Lieu

# Empecher d'afficher à la fois le texte et la zone d'écriture de texte dans les journées.
class SouvenirInline(admin.TabularInline):
    model = Souvenir
    extra = 10
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'180'})},
    }


class JourneeAdmin(admin.ModelAdmin):
    TabularInlines = [SouvenirInline]
    ordering = ["-jour"]

admin.site.register(Journee, JourneeAdmin)
admin.site.register(Souvenir)
admin.site.register(Lieu)
