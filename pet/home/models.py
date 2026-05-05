from django.db import models

# Create your models here.
from django.db import models

class AdminLogin(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'admin_login'  # This tells Django to use the manually created table 'admin_login'

    def __str__(self):
        return self.username


class Animal(models.Model):
    pet_id = models.CharField(max_length=50, unique=True)  # No change
    category = models.CharField(max_length=75)  # Reduced from 100 to 75
    breed = models.CharField(max_length=75)  # Reduced from 100 to 75
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    age = models.IntegerField()
    fur_type = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.pet_id
    
class Bird(models.Model):
    NOICE_CHOICES = [
        ('Quiet', 'Quiet'),
        ('Moderate', 'Moderate'),
        ('Loud', 'Loud'),
       
    ]
    bird_id = models.CharField(max_length=50, unique=True)  # No change
    category = models.CharField(max_length=75)  # Reduced from 100 to 75
    type = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    noice_level = models.CharField(max_length=10, choices=NOICE_CHOICES)

    def __str__(self):
        return self.bird_id
    
class Customer(models.Model):
   
    cust_id = models.CharField(max_length=50, unique=True)  # No change
    name=models.CharField(max_length=75)
    username = models.CharField(max_length=75)  # Reduced from 100 to 75
    phone = models.IntegerField()
    address = models.CharField(max_length=75) 
    password=models.CharField(max_length=75) 

    def __str__(self):
        return self.cust_id
    
class Doctor(models.Model):
   
    doct_id = models.CharField(max_length=50, unique=True)  # No change
    doct_name=models.CharField(max_length=75)
    category = models.CharField(max_length=75)  # Reduced from 100 to 75
   
    hospital = models.CharField(max_length=75) 
    place=models.CharField(max_length=75) 

    def __str__(self):
        return self.doct_id
    
class Appoinment(models.Model):
   
    APT_id = models.CharField(max_length=50, unique=True)  # No change
    pet_name=models.CharField(max_length=75)
    date = models.DateField()  # Reduced from 100 to 75
    time=models.TimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
   
    hospital_name = models.CharField(max_length=75) 
    place=models.CharField(max_length=75) 
    other_query=models.CharField(max_length=100)

    def __str__(self):
        return self.APT_id


