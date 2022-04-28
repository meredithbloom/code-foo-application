from django.urls import path, include 
from . import views



# I included paths for both requesting pure json responses (api) AND for viewing the data in a browser view

app_name = 'media'


urlpatterns = [
    # IN-BROWSER WITH SIMPLE USER NAV
    # master index/homepage includes search bar
    path('', views.masterIndex, name='master_index'),
    path('<int:id>/', views.masterDetail, name='master_detail'),
    path('games/', views.gameIndex, name='game_index'),
    path('movies/', views.movieIndex, name='movie_index'),
    path('comics/', views.comicIndex, name='comic_index'),
    path('tvshows/', views.tvShowIndex, name='tvshow_index'),
    
    # in browser search results
    path('search/', views.searchResults, name='search_results'),
    
    
    # PURE JSON RESPONSES (API)
    
    # api search - include search as query param - 'api/items/search?search='
    path('api/search', views.SearchListView.as_view(), name='api_search_results'),
    
    #get all items (a-z). see additional filters for optional query params. 
    path('api/', views.MediaList.as_view(), name='master_index_api'),
    
    #get all items ordered differently
    path('api/ordered', views.OrderedView.as_view(), name='master_index_ordered_api'),
    
    #show specific item
    path('api/<int:pk>/', views.MediaDetail.as_view(), name='master_detail_api'),
    
    #get all games (a-z), can order by review score with ordering query param
    path('api/games', views.GameList.as_view(), name='game-list-api'),
   
    #get all movies (a-z), can order by review score with ordering query param
    path('api/movies', views.MovieList.as_view(), name='movie-list-api'),
 
    #get all comics (a-z), can order by review score with ordering query param
    path('api/comics', views.ComicList.as_view(), name='comic-list-api'),
    
    # get all tv shows (a-z), can order by review score with ordering query param
    path('api/shows', views.TVShowList.as_view(), name='tv-show-list-api'),
    
   
    
    
    
    

    
]



