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


# GAME VIEWS

class GameList(generics.ListAPIView):
    queryset = Media.objects.filter(media_type='Game')
    serializer_class = MediaSerializer
    
    
# class gameIndex(request):
#     queryset = Media.objects.filter(media_type='Game')
#     context = {'category_list': queryset}


class GameDetail(generics.RetrieveAPIView):
    queryset = Media.objects.filter(media_type='Game')
    serializer_class = MediaSerializer
    
    

# movie views

class MovieList(generics.ListAPIView):
    queryset = Media.objects.filter(media_type='Movie')
    serializer_class = MediaSerializer


class MovieDetail(generics.RetrieveAPIView):
    queryset = Media.objects.filter(media_type='Movie')
    serializer_class = MediaSerializer

# comic views

class ComicList(generics.ListAPIView):
    queryset = Media.objects.filter(media_type='Comic')
    serializer_class = MediaSerializer


class ComicDetail(generics.RetrieveAPIView):
    queryset = Media.objects.filter(media_type='Comic')
    serializer_class = MediaSerializer




# show views

class ShowList(generics.ListAPIView):
    queryset = Media.objects.filter(media_type='Show')
    serializer_class = MediaSerializer


class ShowDetail(generics.RetrieveAPIView):
    queryset = Media.objects.filter(media_type='Show')
    serializer_class = MediaSerializer
