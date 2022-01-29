from django.db import models

# Create your models here.
class Member(models.Model):
    username=models.EmailField(max_length=30)
    password=models.CharField(max_length=19)