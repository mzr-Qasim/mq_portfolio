from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Home

class Home_Admin(admin.ModelAdmin):
    list_display = ['first_name','last_name','photo','profession_1','profession_2','profession_3','twitter_link','facebook_link','linkedin_link','github_link','instagram_link','page_title','nav_logo']

admin.site.register(Home,Home_Admin)  