from django.db import models
from django.contrib.auth.models import User
from .views import k
# Create your models here.
class Answer(models.Model):
    user=models.OneToMany(User,models.CASCADE)
    answer=models.CharField(max_length=100)