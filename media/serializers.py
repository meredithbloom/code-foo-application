from rest_framework import serializers
from .models import Media

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media 
        fields = ('id', 'media_type', 'name', 'long_description', 'short_description', 'created_at', 'updated_at', 'review_url', 'review_score', 'slug', 'genres', 'created_by', 'published_by', 'franchises', 'regions',)
        
        

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('name', 'genres')
        
        
        
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('name','published_by')