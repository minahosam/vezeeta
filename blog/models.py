from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from taggit.managers import TaggableManager
# Create your models here.
day=[('sat','sat'),
('sun','sun'),('mon','mon'),('tues','tues'),('wed','wed'),('thur','thur'),('fri','fri')]
class Post(models.Model):
    title=models.CharField(max_length=50,default='',unique=True)
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
        return self.title
class comments(models.Model):
    commented_post=models.ForeignKey(Post,to_field='title',related_name='post_comment',on_delete=models.CASCADE)
    author=models.ForeignKey(User,related_name='author',on_delete=models.CASCADE)
    comment_date=models.DateField(auto_now_add=True)
    content=models.TextField(max_length=500,null=True,blank=True)
    def __str__(self):
        return str(self.author)   
class reply(models.Model):
    reply_post=models.ForeignKey(comments,related_name='reply_post',null=True,blank=True,on_delete=models.CASCADE)
    reply_author=models.ForeignKey(User,related_name='reply_author',on_delete=models.CASCADE)
    reply_time=models.TimeField(auto_now=True)
    content=models.TextField(max_length=100,blank=True,null=True)
    def children(self):
        return reply.objects.filter(reply_post=comments)
    @property
    def is_parent(self):
        if self.is_parent is not None:
            return False
        return True