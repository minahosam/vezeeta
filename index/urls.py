from django.urls import path
from . import views
app_name='index'
urlpatterns=[
    path('',views.home,name='index'),
    path('search/',views.search_res,name='search'),
    path('home/<str:slug>/',views.detail,name='detail'),
    path('reservation/',views.reservation,name='reservation'),
    path('subscribed_mails/',views.subscribed_mail,name='subscribed'),
    path('my-reservation/',views.my_reservtion,name='my_reservation'),
]