from django.urls import path
from blogs.views import *

app_name = "blogs"

urlpatterns = [
  path('<int:pid>', blog, name="blog"),
  path('blog-list/', blog_lists, name="blog-list"),
  path('category/<str:cat_name>', blog_lists, name="blog-category"),
  path('author/<str:author_name>', blog_lists, name="blog-author"),
  path('tag/<str:tag_name>', blog_lists, name="blog-tag"),
  path('search/',blog_search, name="blog-search"),
  path('add-blog', add_blog, name="add-blog"),
  path('remove-blog', remove_blog, name="remove-blog"),
  path('manage-blogs', manage_blogs, name="manage-blogs"),
  path('test', test, name="test"),
  path('test2-<int:pid>', test2, name="test2")
]