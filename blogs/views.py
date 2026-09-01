from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.

def add_blog(request):
  return render(request, "manage-blogs/add_blogs.html")

def remove_blog(request):
  return render(request, "manage-blogs/remove_blogs.html")

def manage_blogs(request):
  return render(request, "manage-blogs/manage_blogs.html")


def blog_lists(request,**kwargs):
  posts = Post.objects.filter(status = 1)
  if kwargs.get("cat_name") != None:
    posts = posts.filter(category__name = kwargs["cat_name"])
  if kwargs.get("author_name") != None:
    posts = posts.filter(author__username = kwargs["author_name"])
  context = {"posts":posts}
  return render(request, "blogs/blog-home.html", context)

def blog(request, pid):
  posts = Post.objects.filter(status = 1)
  post = get_object_or_404(posts , pk=pid)
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