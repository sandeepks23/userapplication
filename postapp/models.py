from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Posts(models.Model):
    post_owner=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    text_content=models.TextField(max_length=500)
    likes=models.ManyToManyField(User,blank=True,related_name='likes')
    like_count=models.IntegerField(default=0)
    date=models.DateField(auto_now=True)

    def __str__(self):
        return self.post_owner.username

