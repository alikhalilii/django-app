from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.

def add_blog(request):
  return render(request, "manage-blogs/add_blogs.html")

def remove_blog(request):
  return render(request, "manage-blogs/remove_blogs.html")

def manage_blogs(request):
  return render(request, "manage-blogs/manage_blogs.html")


def blog_lists(request):
  posts = Post.objects.all()
  context = {"posts":posts}
  return render(request, "blogs/blog-home.html", context)

def blog(request, pid):
  post = get_object_or_404(Post , pk=pid)
  context = {"post":post}
  return render(request, "blogs/blog-single.html", context)

def test(request):
  posts = Post.objects.all()
  context = {"posts":posts}
  return render(request,"test.html", context)

def test2(request , pid):
  post = get_object_or_404(Post , pk=pid)
  context = {"post":post}
  return render(request,"test2.html", context)