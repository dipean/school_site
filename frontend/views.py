from django.shortcuts import render
from .models import Category,Post

def home(request):
    # categories=Category.objects.all()
    # course=Category.objects.filter()
    # context={
    #     "categories":categories,
    # }
    return render(request,"frontend/home.html")


def category_detail(request,id):
    ctg=Category.objects.filter(id=id).first()
    context={
        "category":ctg
    }
    return render(request,"frontend/category.html",context)

def post_detail(request,id):
    post=Post.objects.filter(id=id).first()
    context={
        "post":post
    }
    return render(request,"frontend/post.html",context)


