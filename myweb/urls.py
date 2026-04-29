from django.urls import path
from myweb.views import *

urlpatterns = [
  path('', home_view),
  path('about', about_view),
  path('contact', contact_view),
  path('elements', elements_view)
]