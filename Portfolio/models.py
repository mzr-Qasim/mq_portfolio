from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name  # Ensure category name is shown in the admin and forms

    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Categories"  # Plural name (same as singular, to avoid pluralization)


# Create your models here.
class Portfolio(models.Model):
    title = models.TextField(max_length=30,null=True,blank=True)
    image= models.FileField(max_length=200 , upload_to="Portfolio/", null=True,blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


 
    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Portfolio"  # Plural name (same as singular, to avoid pluralization)