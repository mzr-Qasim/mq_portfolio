from django.contrib import admin

# Register your models here.
from .models import Skills

class Skills_Admin(admin.ModelAdmin):
    list_display = ['skill_1_name','skill_1_percentage','skill_2_name','skill_2_percentage','skill_3_name','skill_3_percentage','skill_4_name','skill_4_percentage','skill_5_name','skill_5_percentage','skill_6_name','skill_6_percentage']

admin.site.register(Skills,Skills_Admin)  