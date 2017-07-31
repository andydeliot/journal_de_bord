from django.contrib import admin
from .models import Journee, Souvenir

# Register your models here.

class SouvenirInline(admin.TabularInline):
    model = Souvenir
    extra = 0
    max_num = 1
    

class JourneeAdmin(admin.ModelAdmin):
    inlines = [SouvenirInline]
    # date_hierarchy = "jour"
    # ordering = ["jour"]
    search_fields = ["jour"]

admin.site.register(Journee, JourneeAdmin)
admin.site.register(Souvenir)
