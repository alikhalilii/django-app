from django.urls import path
from blogs.views import *

urlpatterns = [
  path('blog', blog),
  path('blog-list', blog_lists),
  path('add-blog', add_blog),
  path('remove-blog', remove_blog),
  path('manage-blogs', manage_blogs)
]