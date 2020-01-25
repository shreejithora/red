from django.db import models

# Create your models here.

GENDER_MALE = 0
GENDER_FEMALE = 1
GENDER_NOT_SPECIFIED = 2

GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]

class UserModel(models.Model):
    name = models.CharField(max_length=120) 
    email = models.EmailField()
    gender = models.IntegerField(choices=GENDER_CHOICES, default=GENDER_NOT_SPECIFIED)
    password = models.CharField(max_length=120)

    def __str__(self):
        return(self.name)
