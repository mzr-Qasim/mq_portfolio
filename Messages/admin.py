from django.contrib import admin

# Register your models here.
from .models import Messages

class MessagesAdmin(admin.ModelAdmin):
    list_display=['name','email','messagesubject', 'message']

admin.site.register(Messages, MessagesAdmin)
