from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeRender, name='home')
]