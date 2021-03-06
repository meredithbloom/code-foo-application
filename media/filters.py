import django_filters
from rest_framework import filters
from rest_framework import generics
from .models import Media



class MediaFilter(django_filters.FilterSet):
    media_type = django_filters.CharFilter(field_name='media_type', lookup_expr='icontains')
    genre = django_filters.CharFilter(field_name='genres', lookup_expr='icontains')
    
    min_rating = django_filters.NumberFilter(field_name='review_score', lookup_expr='gte')
    max_rating = django_filters.NumberFilter(field_name='review_score', lookup_expr='lte')
    
    created_by = django_filters.CharFilter(field_name='created_by', lookup_expr='icontains')
    publisher = django_filters.CharFilter(field_name='published_by', lookup_expr='icontains')
    
    class Meta:
        model = Media 
        fields = ['media_type', 'genre', 'min_rating', 'max_rating', 'created_by', 'publisher']

    