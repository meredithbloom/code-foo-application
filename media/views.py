from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.template import loader
from .models import Media
from rest_framework import generics, filters 
from .serializers import MediaSerializer
import django_filters
from .filters import MediaFilter



# GENERAL VIEWS 

# all items (index)
class MediaList(generics.ListAPIView):
    queryset = Media.objects.all().order_by('id')
    serializer_class = MediaSerializer
    # filter class includes optional query params for media type, genre, min rating, max rating
    filter_class = MediaFilter
    

class SearchListView(generics.ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'short_name', 'slug']


# specific item (show)
class MediaDetail(generics.RetrieveAPIView):
    queryset = Media.objects.all().order_by('id')
    serializer_class = MediaSerializer


# trying to figure out how to include both content filters and ordering in same view
class OrderedView(generics.ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'name', 'review_score']


def masterIndex(request):
    queryset = Media.objects.all().order_by('id')
    serializer_class = MediaSerializer
    context = {'item_list': queryset,
               'name': 'Master Index',
               'sorting': 'Sorted by A-Z (All)'}
    return render(request, 'media/index.html', context)


def searchResults(request):
    serializer_class = MediaSerializer
    query = request.GET.get('q')
    item_list = Media.objects.filter(name__icontains=query)
    context = {'item_list': item_list}
    return render(request, 'media/search_results.html', context)


def masterDetail(request, id):
    try:
        queryset = Media.objects.get(id=id)
    except Media.DoesNotExist:
        raise Http404("Entry does not exist.")
    return render(request, 'media/detail.html', {'item': queryset})


# FILTERED VIEWS (by media type)

# GAME VIEWS
# all games, ordered by id (A-Z) or review score
class GameList(generics.ListAPIView):
    queryset = Media.objects.filter(media_type='Game')
    serializer_class = MediaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'name', 'review_score']
    

def gameIndex(request):
    queryset = Media.objects.filter(media_type='Game').order_by('id')
    serializer_class = MediaSerializer
    context = {'item_list': queryset,
               'name': 'Video Games',
               'sorting': 'Sorted by A-Z (All)'}
    return render(request, 'media/index.html', context)


# MOVIE VIEWS
# all movies, ordered by id (A-Z) or review score
class MovieList(generics.ListAPIView):
    queryset = Media.objects.filter(media_type='Movie')
    serializer_class = MediaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'name', 'review_score']


def movieIndex(request):
    queryset = Media.objects.filter(media_type='Movie').order_by('id')
    serializer_class = MediaSerializer
    context = {'item_list': queryset,
               'name': 'Movies',
               'sorting': 'Sorted by A-Z (All)'}
    return render(request, 'media/index.html', context)


# COMIC VIEWS
# all comics, ordered by id (A-Z) or review score
class ComicList(generics.ListAPIView):
    queryset = Media.objects.filter(media_type='Comic')
    serializer_class = MediaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'name', 'review_score']
    
    
def comicIndex(request):
    queryset = Media.objects.filter(media_type='Comic').order_by('id')
    serializer_class = MediaSerializer
    context = {'item_list': queryset,
               'name': 'Comics',
               'sorting': 'Sorted by A-Z (All)'}
    return render(request, 'media/index.html', context)


# TV SHOW VIEWS
# all tv shows, ordered by id (A-Z) or review score
class TVShowList(generics.ListAPIView):
    queryset = Media.objects.filter(media_type='Show')
    serializer_class = MediaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'name', 'review_score']
    
    
def tvShowIndex(request):
    queryset = Media.objects.filter(media_type='Show').order_by('id')
    serializer_class = MediaSerializer
    context = {'item_list': queryset,
               'name': 'TV Shows',
               'sorting': 'Sorted by A-Z (All)'}
    return render(request, 'media/index.html', context)







