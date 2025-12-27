from django.contrib import admin

# Register your models here.
from .models import Services

class Services_Admin(admin.ModelAdmin):
    list_display = ['title','description','icon']

admin.site.register(Services,Services_Admin)  