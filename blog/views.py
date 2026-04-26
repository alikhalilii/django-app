from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def add_blog(request):
  return HttpResponse("<h1>Please add your blog</h1>")

def blog_lists(request):
  return HttpResponse("<h1>choose from our blogs</h1>")

def blog(request):
  return HttpResponse("<h1>blog ...</h1>")