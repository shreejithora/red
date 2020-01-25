from django.db import models

# Create your models here.

class DateCategoryModel(models.Model):
    cat_title = models.CharField(max_length=120)

    def __str__(self):
        return(self.cat_title)

# GENDER_MALE = 0
# GENDER_FEMALE = 1
# GENDER_NOT_SPECIFIED = 2

# GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]

class DonateModel(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=120)
    address = models.CharField(max_length=255)
    datecategory = models.ForeignKey(DateCategoryModel,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return(self.name)