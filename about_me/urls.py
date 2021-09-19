from django.urls import path, include
from .views import *

app_name = 'about_me'
urlpatterns = [
    path('', about_me_page_view, name='about_me'),
]
