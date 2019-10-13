from django.db import models

# Create your models here.
class Item(models.Model):
    business = models.CharField(max_length=100, blank=False)
    manager = models.CharField(max_length=50, blank=False)
    feedback = models.TextField(max_length=200, blank=False)
    date = models.DateField()
    
    
    def __str__(self):
        return self.business
        
