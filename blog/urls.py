from django.urls import path
from . import views
app_name='blog'
urlpatterns = [
    path('all/',views.blog_list,name='list'),
    path('search/',views.post_search,name='search'),
    path('<int:id>/',views.blog_detail,name='detail'),
    path('new_post/',views.new_post,name='new'),
    path('<int:id>/update',views.update_post,name='update'),
    path('<int:id>/delete',views.delete_post,name='delete'),
    path('<int:id>/like',views.like,name='like'),
    path('<int:id>/likee',views.like_with_ajax,name='ajax')
]
