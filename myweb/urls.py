from django.urls import path
from myweb.views import *

urlpatterns = [
  path('', home_view),
  path('about-us', about_view)
]