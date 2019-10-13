from django.db import models
from services.models import Service
# Create your models here.

class Order(models.Model):
    date = models.DateField()
    business_name = models.CharField(max_length=50, blank=False)
    project_name = models.CharField(max_length=50, blank=False)
    design_information1 = models.TextField(blank=False)
    design_information2 = models.TextField(blank=False)
    design_information3 = models.TextField(blank=False)
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.service.title, self.service.price)
