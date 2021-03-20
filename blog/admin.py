from django.contrib import admin
from .models import Post , comments , reply
# Register your models here.
admin.site.register(Post)
admin.site.register(comments)
admin.site.register(reply)