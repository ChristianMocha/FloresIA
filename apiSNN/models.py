from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to ='foto/', null=True)
    label = models.CharField(max_length=100)
    probability = models.FloatField()