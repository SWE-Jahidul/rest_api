from  django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    descripction = models.CharField(max_length=100)


    def __str__(self):
        return self.title
    
