from django.urls import path
from myweb.views import *

urlpatterns = [
  path('home', home_view),
  path('about-us', about_view)
]