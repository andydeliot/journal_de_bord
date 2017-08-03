from django.contrib import admin
from .models import Journee, Souvenir

# Register your models here.

class SouvenirInline(admin.TabularInline):
    model = Souvenir
    extra = 10
    

class JourneeAdmin(admin.ModelAdmin):
    inlines = [SouvenirInline]

admin.site.register(Journee, JourneeAdmin)
admin.site.register(Souvenir)
