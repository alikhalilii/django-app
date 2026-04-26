from django.urls import path
from blog.views import *

urlpatterns = [
  path('blog', blog),
  path('blog-list', blog_lists),
  path('add-blog', add_blog)
]