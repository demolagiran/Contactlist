from django.db import models

# Create your models here.

class Mycontact(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=15)
    emailAddress = models.EmailField()
    address = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Mycontact'
