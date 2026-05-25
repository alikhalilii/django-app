from django.urls import path
from blogs.views import *

app_name = "blogs"

urlpatterns = [
  path('blog', blog, name="blog"),
  path('blog-list', blog_lists, name="blog-list"),
  path('add-blog', add_blog, name="add-blog"),
  path('remove-blog', remove_blog, name="remove-blog"),
  path('manage-blogs', manage_blogs, name="manage-blogs"),
  path('test', test, name="test"),
  path('test2-<int:pid>', test2, name="test2")
]