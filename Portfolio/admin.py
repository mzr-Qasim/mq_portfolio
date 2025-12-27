from django.contrib import admin

# Register your models here.
from django import forms
from .models import Portfolio, Category

class PortfolioAdminForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),  # Fetch all categories from the database
        widget=forms.SelectMultiple,  # Display categories in a multi-select dropdown
        required=False  # Make the field optional
    )

    class Meta:
        model = Portfolio
        fields = '__all__'  # Include all fields from the Portfolio model in the form




class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  # Display name and slug in the list view
    search_fields = ('name',)  # Enable search functionality by category name
    prepopulated_fields = {'slug': ('name',)}  # Automatically generate a slug from the name

admin.site.register(Category, CategoryAdmin)






class Portfolio_Admin(admin.ModelAdmin):
    list_display = ['title','get_categories','image']
    list_filter = ('categories',)  # Add a filter sidebar for categories
    search_fields = ('title', 'description')  # Enable search functionality by title and description


    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    get_categories.short_description = 'Categories'  # Display a custom column name in the admin list
    

admin.site.register(Portfolio,Portfolio_Admin)  