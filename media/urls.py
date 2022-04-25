from django.urls import path, include 
from . import views


# I included paths for both requesting pure json responses (api) AND for viewing the data in a browser view

app_name = 'media'


urlpatterns = [
    # IN-BROWSER WITH SIMPLE USER NAV
    path('', views.masterIndex, name='master_index'),
    path('<int:id>/', views.masterDetail, name='master_detail'),
    
    
    # PURE JSON RESPONSES
    
    #get all items (a-z)
    path('api/items', views.MediaList.as_view(), name='master_index_api'),
    #get all items (review score, descending)
    path('api/items/rating', views.MediaListByRating.as_view(), name='all-by-rating'), 
    #show specific item
    path('api/items/<int:pk>/', views.MediaDetail.as_view(), name='master_detail_api'),
    
    #get all games (a-z)
    path('api/items/games', views.GameList.as_view(), name='game-list'),
    
    path('api/items/games/<int:pk>', views.GameDetail.as_view(), name='game-detail'),
    
    path('api/items/movies', views.MovieList.as_view(), name='movie-list'),
    path('api/items/movies/<int:pk>', views.MovieDetail.as_view(), name='movie-detail'),

    path('api/items/comics', views.ComicList.as_view(), name='comic-list'),
    path('api/items/comics/<int:pk>', views.ComicDetail.as_view(), name='comic-detail'),

    # get all shows (a-z)
    path('api/items/shows', views.TVShowList.as_view(), name='tv-show-list'),
    # get all shows (review score, descending)
    path('api/items/shows/rating', views.TVShowListByRating.as_view(), name='tv-show-by-rating'), 
    # get specific show
    path('api/items/shows/<int:pk>', views.TVShowDetail.as_view(), name='tv-show-detail')
    
    
    # SORTING DATA
    
]



