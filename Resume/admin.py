from django.contrib import admin

# Register your models here.
from .models import Resume

class Resume_Admin(admin.ModelAdmin):
    list_display = ['education_title','education_title_details','education_description','experience_title','experience_title_details','experience_description']

admin.site.register(Resume,Resume_Admin)  