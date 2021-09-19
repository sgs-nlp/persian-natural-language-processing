from django.urls import path, include
from .views import *

app_name = 'home'
urlpatterns = [
    path('', home_page_view, name='home'),
]
