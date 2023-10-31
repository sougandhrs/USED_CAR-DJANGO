from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class users(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    u_fname=models.TextField(max_length=50,db_column='firstname',default='null',null=False)
    u_lname=models.TextField(max_length=50,db_column='lastname',default='null',null=False)
    u_dob=models.DateField(db_column='dateofbirth',default='2023-10-02',null=False)
    u_contact=models.CharField(max_length=50,db_column='contactinfo',default='1234567890',null=False)
    u_house=models.TextField(max_length=50,db_column='house',default='null',null=False)
    u_place=models.TextField(max_length=50,db_column='place',default='null',null=False)
    u_pin=models.TextField(max_length=50,db_column='pincode',default='null',null=False)
    u_profile=models.ImageField(upload_to='profile/',db_column='profileimage',default='null',null=False)

    def __str__(self):
        return self.user.username


