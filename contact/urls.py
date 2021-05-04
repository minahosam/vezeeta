from django.urls import path
from .views import contact_info,send
app_name='contact'
urlpatterns = [
    path('',contact_info,name='contact'),
    path('sent/',send,name='sent'),
]
