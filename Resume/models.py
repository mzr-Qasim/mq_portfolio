from django.db import models

# Create your models here.
class Resume(models.Model):
    education_title = models.CharField(max_length=50,null=True,blank=True)
    education_title_details = models.CharField(max_length=50,null=True,blank=True)
    education_description = models.TextField(max_length=300,null=True,blank=True)
    
    experience_title = models.CharField(max_length=50,null=True,blank=True)
    experience_title_details = models.CharField(max_length=50,null=True,blank=True)
    experience_description = models.TextField(max_length=300,null=True,blank=True)

    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Resume"  # Plural name (same as singular, to avoid pluralization)