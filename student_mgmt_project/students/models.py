from django.db import models
from django import forms

# Create your models here.
class Students(models.Model):
    Name = models.CharField(max_length=120)
    Email = models.EmailField(max_length=200)
    Roll_Number = models.IntegerField()
    Department = models.CharField(max_length=120)
    Date_of_Birth = models.DateField()

    def to_dict(self):
        return {
            "Name":self.Name,
            "Email":self.Email,
            "Roll_Number":self.Roll_Number,
            "Department":self.Department,
            "Date_of_Birth":self.Date_of_Birth
        }
class Register(models.Model):
    Name = models.CharField(max_length=120)
    Email = models.EmailField(max_length=200)
    Password = models.CharField(max_length=120)

    def to_dict(self):
        return {
            "Name":self.Name,
            "Email":self.Email,
            "Password":self.Password
        }
    

















    