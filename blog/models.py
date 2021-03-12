from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from taggit.managers import TaggableManager
# Create your models here.
day=[('sat','sat'),
('sun','sun'),('mon','mon'),('tues','tues'),('wed','wed'),('thur','thur'),('fri','fri')]
class Post(models.Model):
    title=models.CharField(max_length=50,null=True,blank=True)
    content=FroalaField()
    post_time=models.TimeField()
    post_day=models.CharField(max_length=5,choices=day,null=True,blank=True)
    post_date=models.DateField()
    tags=TaggableManager()
    view_count=''
    author=models.ForeignKey(User,related_name='post_author',on_delete=models.CASCADE)
    post_image=models.ImageField(upload_to='post_image/')
    like=models.ManyToManyField(User,related_name='user_like')
    add_to_favorite=models.ManyToManyField(User,related_name='user_favorities')
    def __str__(self):
        return str(self.author)
    