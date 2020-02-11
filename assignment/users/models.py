from django.db import models

# Create your models here.
class UserData(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=20)
    company_name=models.CharField(max_length=80)
    age=models.PositiveIntegerField()
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=50)
    zip=models.CharField(max_length=12)
    email=models.EmailField(max_length=200,unique=True)
    web=models.CharField(max_length=100)