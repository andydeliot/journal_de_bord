from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from .models import Journee, Souvenir, Lieu

# Register your models here.

class SouvenirInline(admin.TabularInline):
    model = Souvenir
    extra = 10
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'180'})},
        # models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':150})},
    }


class JourneeAdmin(admin.ModelAdmin):
    inlines = [SouvenirInline]
    # date_hierarchy = "jour"
    ordering = ["-jour"]

admin.site.register(Journee, JourneeAdmin)
admin.site.register(Souvenir)
admin.site.register(Lieu)
