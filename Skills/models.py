from django.db import models

# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.




class Skills(models.Model):
    skill_1_name = models.CharField(max_length=30,null=True,blank=True)
    
    skill_1_percentage = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(100)],null=True,blank=True
    )
    skill_2_name = models.CharField(max_length=30,null=True,blank=True)
    
    skill_2_percentage = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(100)],null=True,blank=True
    )
    skill_3_name = models.CharField(max_length=30,null=True,blank=True)
    
    skill_3_percentage = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(100)],null=True,blank=True
    )
    skill_4_name = models.CharField(max_length=30,null=True,blank=True)
    
    skill_4_percentage = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(100)],null=True,blank=True
    )
    skill_5_name = models.CharField(max_length=30,null=True,blank=True)
    
    skill_5_percentage = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(100)],null=True,blank=True
    )
    skill_6_name = models.CharField(max_length=30,null=True,blank=True)
    
    skill_6_percentage = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(100)],null=True,blank=True
    )



    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Skills"  # Plural name (same as singular, to avoid pluralization)
 



