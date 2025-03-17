from django.db import models
from datetime import datetime 
from django.contrib.auth.models import AbstractBaseUser

# SDA Punjab Model
class SDAPunjab(models.Model): 
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    responsibilities = models.TextField()
    
# SDA Haryana Model 
class SDAHaryana(models.Model): 
    state = models.CharField(max_length=255)
    officer_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    headquarter = models.CharField(max_length=255)
    email = models.EmailField()
    epbx_no = models.CharField(max_length=50)
    
# Govt. Model   
class GovtBuilding(models.Model): 
    department = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    website = models.URLField(blank=True, null=True)
    
# Division Details Model
class DivisionDetail(models.Model):
    division_name = models.CharField(max_length=255)
    drm_name = models.CharField(max_length=255)
    zone_name = models.CharField(max_length=255)
    zone_code = models.CharField(max_length=50)
    no_of_divisions = models.IntegerField()
    no_of_stations = models.IntegerField()
    headquarters = models.CharField(max_length=255)
    address = models.TextField()

# Railways Details Model
class RailwayDetail(models.Model):
    zone = models.CharField(max_length=255)
    division_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

