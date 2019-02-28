from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    author_name = models.CharField(max_length = 200)
    content = models.CharField(max_length = 3000)
    post_date = models.DateTimeField('date posted')

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    nickname = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    content = models.CharField(max_length = 3000)
    post_date = models.DateTimeField('date posted')
