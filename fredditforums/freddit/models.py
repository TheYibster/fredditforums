from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class Thread(models.Model):
    topic = models.CharField(max_length=200)
    inform = models.TextField()
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    author = models.CharField(max_length=18, default='Anonymous')
    slug = models.SlugField()
    
    def __str__(self):
        return self.topic

    def save(self, *args, **kwargs):
        self.slug = slugify(self.topic)
        super(Thread, self).save(*args, **kwargs)

class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    comment = models.TextField()
    likes = models.IntegerField(default=0)
    author = models.CharField(max_length=18, default='Anonymous')

    def __str__(self):
        return self.comment


