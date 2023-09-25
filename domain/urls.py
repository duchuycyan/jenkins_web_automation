from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="domain"),
    path('search/', views.search, name="search"),
]