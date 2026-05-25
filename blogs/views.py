from django.shortcuts import render
from .models import Post

# Create your views here.

def add_blog(request):
  return render(request, "manage-blogs/add_blogs.html")

def remove_blog(request):
  return render(request, "manage-blogs/remove_blogs.html")

def manage_blogs(request):
  return render(request, "manage-blogs/manage_blogs.html")


def blog_lists(request):
  return render(request, "blogs/blog-home.html")

def blog(request):
  return render(request, "blogs/blog-single.html")

def test(request):
  posts = Post.objects.all()
  context = {"posts":posts}
  return render(request,"test.html",context)