from django.urls import path, include
from .views import *

app_name = 'contact_me'
urlpatterns = [
    path('', contact_me_page_view, name='contact_me'),
]
