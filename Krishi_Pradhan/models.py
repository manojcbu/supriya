from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    email = models.EmailField(max_length=100)
    password1 = models.CharField(max_length=45)
    password2 = models.CharField(max_length=45)

class question(models.Model):
    region = models.CharField(max_length=100)
    soil = models.CharField(max_length=100)
    previous = models.CharField(max_length=100)
 
 
class CropData(models.Model):
    region = models.CharField(max_length=100)
    soil = models.CharField(max_length=100)
    previous = models.CharField(max_length=100)

class CropSoil(models.Model):
    region = models.CharField(max_length=100)
    soil_type = models.CharField(max_length=100)
    previous_crop = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.region} - {self.soil} - {self.previous}'

class Meta:
    db_table = 'cropdata'
__all__ = ['User', 'question', 'CropData']
