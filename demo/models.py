from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

class contactModel(models.Model):
    name=models.TextField(max_length=20)
    email=models.TextField(max_length=20)
    address=CKEditor5Field('Text',null=True,blank=True, config_name='extends',)
    
