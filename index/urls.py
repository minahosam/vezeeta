from django.urls import path
from . import views
app_name='index'
urlpatterns=[
    path('',views.home,name='index'),
    path('search/',views.search_res,name='search'),
    path('<str:slug>/',views.detail,name='detail'),
]