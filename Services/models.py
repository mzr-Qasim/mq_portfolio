from django.db import models

# Create your models here.
class Services(models.Model):


    title = models.TextField(max_length=50,null=True)
    description = models.TextField(max_length=120,null=True)   
    icon = models.CharField(max_length=300,null=True)





 
    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Services"  # Plural name (same as singular, to avoid pluralization)