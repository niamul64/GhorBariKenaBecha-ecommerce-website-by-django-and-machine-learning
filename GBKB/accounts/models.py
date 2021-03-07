from django.db import models
from django.contrib.auth.models import User # default user model import
# Create your models here.
from django.utils import timezone

class ExtentionUser(models.Model):  # extra fields for user
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    mobileNumber= models.CharField(max_length=120, default="" , null=False , blank= False)
    image = models.ImageField(upload_to='images/post/', default='demo.png', blank=True)
    activation = models.BooleanField(default=False)
    code= models.IntegerField(default=1, null=True , blank= True)

    def __str__(self):
        return self.userID.username


class PostAd(models.Model):                # for saving the shared news in database
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, default="" , null=False , blank= False)
    location = models.CharField(max_length=120, default="" , null=False , blank= False, choices=(
        ('', 'Location'),
        ('Dhaka Cantonment', 'Dhaka Cantonment'),
        ('Dhamrai', 'Dhamrai'),
        ('Dhanmondi', 'Dhanmondi'),
        ('Gulshan 1', 'Gulshan 1'),
        ('Gulshan 2', 'Gulshan 2'),
        ('Jatrabari', 'Jatrabari'),
        ('Keraniganj', 'Keraniganj'),
        ('Khilgaon', 'Khilgaon'),
        ('Khilkhet', 'Khilkhet'),
        ('Lalbag', 'Lalbag'),
        ('Mohammadpur', 'Mohammadpur'),
        ('Mirpur', 'Mirpur'),
        ('Motijheel', 'Motijheel'),
        ('Palton', 'Palton'),
        ('Ramna', 'Ramna'),
        ('Sabujbag', 'Sabujbag'),
        ('Tejgaon', 'Tejgaon'),
        ('Uttara', 'Uttara'),
        ('Dhanmondi', 'Dhanmondi'),
        ('Boshundhora', 'Boshundhora'),
        ('Bonani', 'Bonani'),
        ('Mohakhali', 'mohakhali'),
        ))
    img1 = models.ImageField(upload_to='images/post', default='demo.png',blank=True)
    img2 = models.ImageField(upload_to='images/post', default='demo.png',blank=True)
    img3 = models.ImageField(upload_to='images/post', default='demo.png',blank=True)
    sqft = models.IntegerField(default=None, null=False , blank= False)
    washRoom = models.IntegerField(default=None, null=False , blank= False)
    bedRoom = models.IntegerField(default=None, null=False , blank= False)
    description = models.TextField(max_length=120, default="", null=True, blank=True)

    roadSize = models.IntegerField(default=None, null=False, blank=False)
    lift = models.IntegerField(null=False , blank= False, choices=(
        (None, 'select'),
        (0,'No Lift'),
        (1,'Lift service available'),
        ))
    floor = models.IntegerField(default=None, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=None, null=False, blank=False)
