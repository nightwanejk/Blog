from django.db import models

# Create your models here.
class Post(models.Model):
    event_image = models.ImageField(upload_to='blog_images/')
    event_date = models.DateField(auto_now=True)
    event_title = models.CharField(max_length=300)
    event_text = models.TextField()