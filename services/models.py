from django.db import models

# Create your models here.
class Service (models.Model):
    
    title = models.CharField(max_length=255)
    service_image = models.ImageField(upload_to='images')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    size = models.TextField()
    information = models.TextField()
    
    def __str__(self):
        return self.title