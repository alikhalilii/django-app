from django import template
from blogs.models import Post
register = template.Library()

@register.simple_tag
def hello():
  return "hello"

@register.simple_tag
def plusTwo(a = 0):
  return a + 2

@register.simple_tag(name="posts")
def function():
  posts = Post.objects.filter(status = 1)
  return posts

@register.simple_tag(name="total_posts")
def function():
  posts_count = Post.objects.filter(status = 1).count()
  return posts_count

@register.filter(name="snippet")
def function(value,limit=20):
  return value[:limit]+ "..."

@register.inclusion_tag("inclusion_tag_test.html",name="inclusion_test")
def function():
  posts = Post.objects.filter(status=1).order_by("published_date")[0:2]
  return {"posts":posts}

# from here the real tags that we use in project will be created

@register.inclusion_tag("blogs/components/blog_popular_posts.html")
def latestposts(arg=3):
  posts = Post.objects.filter(status=1).order_by("published_date")[:arg]
  return {"posts":posts}