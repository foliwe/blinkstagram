
from django.urls import path
from .views import home, create, delete_post, update_post, post_detail  # cagetory_list

urlpatterns = [
    path('', home, name="home"),
    path('create/', create, name="create"),
    path('delete_post/<pk>', delete_post, name="delete_post"),
    path('update_post/<pk>', update_post, name="update_post"),
    path('post_detail/<pk>', post_detail, name="post_detail"),
    path('categories/<tag>', home, name='categories')
]
