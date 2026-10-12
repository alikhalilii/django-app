from django.shortcuts import render,get_object_or_404
from .models import Post , Comment
from blogs.forms import CommentForm
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import HttpResponseRedirect
from django.urls import reverse


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
  if kwargs.get("tag_name") != None:
    posts = posts.filter(tags__name__in=[kwargs["tag_name"]])
  posts = Paginator(posts , 3)
  try:
    page_number = request.GET.get('page')
    posts = posts.get_page(page_number)
  except PageNotAnInteger:
    posts = posts.get_page(1)
  except EmptyPage:
    posts = posts.get_page(1)
  context = {"posts":posts}
  return render(request, "blogs/blog-home.html", context)

def blog(request, pid):
  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid:
      form.save()
      messages.add_message(request,messages.SUCCESS,"your comment submited successfully!")
    else:
      messages.add_message(request,messages.ERROR,"your comment didnt submited")
  posts = Post.objects.filter(status = 1)
  post = get_object_or_404(posts , pk=pid)
  comments = Comment.objects.filter(post=post.id, is_approved=True)
  form = CommentForm()
  context = {"post":post,"comments":comments, "form":form}
  if not post.login_required:
    return render(request, "blogs/blog-single.html", context)
  else:
    if not request.user.is_authenticated:
      return HttpResponseRedirect(reverse("accounts:login"))
    else:
      return render(request, "blogs/blog-single.html", context)

def blog_search(request):
  posts = Post.objects.filter(status = 1)
  if request.method == "GET":
    if s := request.GET.get('s'):
      posts = posts.filter(content__contains = s )
  context = {"posts":posts}
  return render(request, "blogs/blog-home.html", context)

def test(request):
  posts = Post.objects.all()
  context = {"posts":posts}
  return render(request,"test.html", context)

def test2(request , pid):
  post = get_object_or_404(Post , pk=pid)
  context = {"post":post}
  return render(request,"test2.html", context)