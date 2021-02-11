from django.db import models

# Create your models here.
class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    address  = models.TextField()

    def __str__(self):
        return self.full_name