from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

# Create your models here.

def validate_pdf(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError('Only PDF files are allowed.')


class About(models.Model):
    introduction = models.TextField(max_length=150,null=True,blank=True)
    introduction_description = models.TextField(max_length=400,null=True,blank=True)
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(99)]
    )

    city = models.CharField(max_length=20,null=True,blank=True)
    country = models.CharField(max_length=20,null=True,blank=True) 
    cv = models.FileField(upload_to='CV/', null=True, validators=[validate_pdf])
    photo = models.FileField(max_length=200 , upload_to="Profile_photo", null=True)




 
    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "About Section"  # Plural name (same as singular, to avoid pluralization)