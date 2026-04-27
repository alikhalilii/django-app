from django.shortcuts import render

# Create your views here.

def add_blog(request):
  return render(request, "manage-blogs/add_blogs.html")

def remove_blog(request):
  return render(request, "manage-blogs/remove_blogs.html")

def manage_blogs(request):
  return render(request, "manage-blogs/manage_blogs.html")


def blog_lists(request):
  return render(request, "blogs/blogs.html")

def blog(request):
  return render(request, "blogs/single_blog.html")