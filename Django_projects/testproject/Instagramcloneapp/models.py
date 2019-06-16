from django.db import models

# Create your models here.
class UserModel(models.Model):
    """ 
    This class is for sign up page where user have to provide his/her info
    """
    username = models.CharField(max_length=80)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    password = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)