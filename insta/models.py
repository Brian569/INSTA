from django.db import models
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    name = models.CharField(max_length=10, blank=True)
    profile_pic = CloudinaryField('image')
    bio = models.CharField(max_length=500)
    

    def __str__(self):
        return self.name
    
    def save_profile(self):
        self.save()

class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=100)
    image_caption = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.IntegerField()
    comments = models.TextField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)
    follows = models.IntegerField()

    def __str__(self):
        return self.image_name

    class Meta:
        verbose_name_plural = 'Images'
        ordering = ['pub_date']