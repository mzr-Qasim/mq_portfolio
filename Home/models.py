from django.db import models

# Create your models here.
class Home(models.Model):
    first_name = models.CharField(max_length=10,null=True,blank=True)
    last_name = models.CharField(max_length=10,null=True,blank=True)
    photo= models.FileField(max_length=200 , upload_to="Profile_photo", null=True)

    profession_1 = models.CharField(max_length=20,null=True,blank=True)
    profession_2 = models.CharField(max_length=20,null=True,blank=True)
    profession_3 = models.CharField(max_length=20,null=True,blank=True)
    
    twitter_link = models.CharField(max_length=300,null=True,blank=True)
    facebook_link = models.CharField(max_length=300,null=True,blank=True)
    linkedin_link = models.CharField(max_length=300,null=True,blank=True)
    github_link = models.CharField(max_length=300,null=True,blank=True)
    instagram_link = models.CharField(max_length=300,null=True,blank=True)
    
    page_title = models.CharField(max_length=50,null=True,blank=True)
    nav_logo = models.FileField(max_length=200 , upload_to="Nav_Logo/", null=True,blank=True)




 
    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Home Page"  # Plural name (same as singular, to avoid pluralization)