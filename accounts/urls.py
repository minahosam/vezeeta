from django.urls import path
from .views import signup,profile
app_name='account'
urlpatterns = [
 path('signup/',signup,name='signup'),
 path('profile/',profile,name='profile'),
]
