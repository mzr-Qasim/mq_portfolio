from django.contrib import admin

# Register your models here.
from .models import Contact

class Contact_Admin(admin.ModelAdmin):
    list_display = ['contact_info','location','phone_number']

admin.site.register(Contact,Contact_Admin) 