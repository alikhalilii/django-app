from django.urls import path
from myweb.views import *

app_name = "myweb"
urlpatterns = [
  path('', home_view, name="home"),
  path('about', about_view, name="about"),
  path('contact', contact_view, name="contact"),
  path('elements', elements_view, name="elements")
]