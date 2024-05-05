from django.urls import path
from .views import home,post_detail,category_detail,post_detail

urlpatterns = [
    path("",home,name="home"),
    path("category/<int:id>/",category_detail,name="category_detail"),
    path("post/<int:id>",post_detail,name="post_detail") 
]

