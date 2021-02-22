from django.db import models

# Create your models here.
class footer(models.Model):
    email = models.EmailField(max_length=50,blank=True, null=True)
    phone_number=models.CharField(max_length=20,blank=True,null=True)
    location=models.CharField(max_length=50,blank=True,null=True)
    fb_link=models.URLField(max_length=200,blank=True,null=True)
    youtube_link=models.URLField(max_length=200,blank=True,null=True)
    instgram_link=models.URLField(max_length=200,blank=True,null=True)
    twitter_link=models.URLField(max_length=200,blank=True,null=True)
    