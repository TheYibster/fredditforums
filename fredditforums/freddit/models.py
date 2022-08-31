from pyexpat import model
from django.db import models

# Create your models here.

class Thread(models.Model):
    topic = models.CharField(max_length=200)
    inform = models.TextField()
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.thread_text

class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    comment = models.TextField()
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text


