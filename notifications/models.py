from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification (models.Model):
    
    project = models.CharField(max_length=250)
    message = models.TextField()
    image = models.ImageField(upload_to='images')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
    
    def __str__(self):
        return self.project
