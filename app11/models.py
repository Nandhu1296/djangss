from django.db import models

# Create your models here.

class post(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    phone_number = models.IntegerField()
    #number_of_people = models.IntegerField()


def __str__(self):
    return self.name 




