#from django.shortcuts import render
from rest_framework import generics
from .models import post
from .serializers import PostSerializer 

class postlists(generics.ListAPIView):
    queryset = post.objects.all()
    serializer_class = PostSerializer

class postDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset= post.objects.all()
    serializer_class = PostSerializer



