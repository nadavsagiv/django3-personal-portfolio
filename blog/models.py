from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='blog/images/', blank=True)
    textbox =  models.TextField()
    
    
    def __str__(self):
        return self.title

