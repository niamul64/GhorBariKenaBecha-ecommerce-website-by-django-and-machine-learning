from django.db import models
from django.contrib.auth.models import User # default user model import
# Create your models here.
from django.utils import timezone



class Review(models.Model):  # extra fields for user
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.IntegerField(null=False , blank= False)

    sqft = models.IntegerField(default=1, null=False, blank=False)
    washRoom = models.IntegerField(default=1, null=False, blank=False)
    bedRoom = models.IntegerField(default=1, null=False, blank=False)

    roadSize = models.IntegerField(default=1, null=False, blank=False)
    lift = models.IntegerField(default=1, null=False, blank=False)
    floor = models.IntegerField(default=1, null=False, blank=False)

    price = models.IntegerField(default=1, null=False, blank=False)




class DataSet(models.Model):  # extra fields for user

    location = models.IntegerField(null=False, blank=False)

    sqft = models.IntegerField(default=1, null=False, blank=False)
    washRoom = models.IntegerField(default=1, null=False, blank=False)
    bedRoom = models.IntegerField(default=1, null=False, blank=False)

    roadSize = models.IntegerField(default=1, null=False, blank=False)
    lift = models.IntegerField(default=1, null=False, blank=False)
    floor = models.IntegerField(default=1, null=False, blank=False)

    price = models.IntegerField(default=1, null=False, blank=False)
