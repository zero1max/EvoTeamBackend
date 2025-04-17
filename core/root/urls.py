from django.urls import path
from .views import NewsView, NewsDetailView, BlogView, BlogDetailView

urlpatterns = [
    path('news/', NewsView.as_view(), name='news'),
    path('news/<slug:slug>/', NewsDetailView.as_view(), name='news_detail_url'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail_url'),
]
