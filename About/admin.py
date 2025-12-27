from django.contrib import admin

# Register your models here.
from .models import About

class About_Admin(admin.ModelAdmin):
    list_display = ['introduction','introduction_description','email','age','city','country','cv','photo']

admin.site.register(About,About_Admin)  