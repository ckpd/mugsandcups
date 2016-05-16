from django.db import models
from django.utils import timezone
# Create your models here.

class Testimonial(models.Model):
    title = models.CharField(max_length=250)
    client_logo = models.FileField()
    
    def __str__(self):
        return self.title

class Feature(models.Model):
    title = models.CharField(max_length=250)
    feature_image = models.FileField()
    
    def __str__(self):
        return self.title
    
class Catalog(models.Model):
    title = models.CharField(max_length=250)
    catalog_image = models.FileField()
    data_categories = models.CharField(max_length=250)

    
    def __str__(self):
        return self.title
    