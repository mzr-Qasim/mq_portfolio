from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Contact(models.Model):
    contact_info = models.TextField(max_length=150,null=True,blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    phone_number = models.CharField(
        max_length=11,  
        validators=[
            RegexValidator(
                regex=r'^\+92[3-9][0-9]{9}$|^(0[3-9]{1}[0-9]{2})[ -]?[0-9]{7}$', 
                message="Enter a valid phone number."
            )
        ],
        null=True,
        blank=True
    )





 
    class Meta:
        verbose_name = ""  # Singular name
        verbose_name_plural = "Contact"  # Plural name (same as singular, to avoid pluralization)