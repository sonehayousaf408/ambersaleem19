from django.test import TestCase

# Create your tests here.
from django.db import models
from library.models import Customer

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.customer.name} - {self.total} on {self.date}"
