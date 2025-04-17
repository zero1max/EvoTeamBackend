from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
#
from .models import News, Blog
from .serializers import NewsSerializer, BlogSerializer


class NewsView(APIView):

    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)


class NewsDetailView(APIView):
     
     def get(self, request, slug):
        doctor = get_object_or_404(News, slug=slug)
        serializer = NewsSerializer(doctor)
        return Response(serializer.data)
     
    
class BlogView(APIView):

    def get(self, request):
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data)


class BlogDetailView(APIView):
     
     def get(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)