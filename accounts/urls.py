from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path ('registration/', UserCreate.as_view(), name='registration_url'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
