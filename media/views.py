from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Media
from rest_framework import generics 
from .serializers import MediaSerializer



# Create your views here.

# GENERAL VIEWS (unfiltered)

class MediaList(generics.ListAPIView):
    queryset = Media.objects.all().order_by('id')
    serializer_class = MediaSerializer
    

def masterIndex(request):
    queryset = Media.objects.all().order_by('id')
    serializer_class = MediaSerializer
    context = {'item_list': queryset}
    return render(request, 'media/index.html', context)



class MediaDetail(generics.RetrieveAPIView):
    queryset = Media.objects.all().order_by('id')
    serializer_class = MediaSerializer


def masterDetail(request, id):
    try:
        queryset = Media.objects.get(id=id)
    except Media.DoesNotExist:
        raise Http404("Entry does not exist.")
    return render(request, 'media/detail.html', {'item': queryset})


# FILTERED VIEWS (by media type)
# GAME VIEWS

class GameList(generics.ListAPIView):
    queryset = Media.objects.filter(media_type='Game')
    serializer_class = MediaSerializer
    

def gameIndex(request):
    queryset = Media.objects.filter(media_type='Game').order_by('-review_score')
    serializer_class = MediaSerializer
    context = {'item_list': queryset}
    return render(request, 'media/index.html', context)

# class gameIndex(request):
#     queryset = Media.objects.filter(media_type='Game')
#     context = {'category_list': queryset}


class GameDetail(generics.RetrieveAPIView):
    queryset = Media.objects.filter(media_type='Game')
    serializer_class = MediaSerializer
    
    

# MOVIE VIEWS

class MovieList(generics.ListAPIView):
    queryset = Media.objects.filter(media_type='Movie')
    serializer_class = MediaSerializer


class MovieDetail(generics.RetrieveAPIView):
    queryset = Media.objects.filter(media_type='Movie')
    serializer_class = MediaSerializer

# COMIC VIEWS

class ComicList(generics.ListAPIView):
    queryset = Media.objects.filter(media_type='Comic')
    serializer_class = MediaSerializer

class ComicListByRating(generics.ListAPIView):
    queryset = Media.objects.filter(media_type='Comic').order_by('-review_score')
    serializer_class = MediaSerializer

class ComicDetail(generics.RetrieveAPIView):
    queryset = Media.objects.filter(media_type='Comic')
    serializer_class = MediaSerializer


# TV SHOW VIEWS

# all tv shows, ordered by id (A-Z)
class TVShowList(generics.ListAPIView):
    queryset = Media.objects.filter(media_type='Show')
    serializer_class = MediaSerializer
    
# all tv shows, ordered by rating (descending)    
class TVShowListByRating(generics.ListAPIView):
    queryset = Media.objects.filter(media_type='Show').order_by('-review_score')
    serializer_class = MediaSerializer

# tv show detail
class TVShowDetail(generics.RetrieveAPIView):
    queryset = Media.objects.filter(media_type='Show')
    serializer_class = MediaSerializer


# SORTING VIEWS

class MediaListByRating(generics.ListAPIView):
    queryset = Media.objects.all().order_by('-review_score')
    serializer_class = MediaSerializer