# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.postlists.as_view()),
    path('<int:pk>/', views.postDetails.as_view()),

]