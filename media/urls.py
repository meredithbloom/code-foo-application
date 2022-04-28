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
    
    # api search
    path('api/items/search', views.SearchListView.as_view(), name='api_search_results'),
    # include search as query param
    # 'api/items/search?search='
    
    #get all items (a-z). see additional filters for optional query params
    path('api/items', views.MediaList.as_view(), name='master_index_api'),
    
    #get all items (review score, descending)
    path('api/items/rating', views.MediaListByRating.as_view(), name='all-by-rating-api'), 
    #show specific item
    path('api/items/<int:pk>/', views.MediaDetail.as_view(), name='master_detail_api'),
    
    #get all games (a-z)
    path('api/items/games', views.GameList.as_view(), name='game-list-api'),
    #get all games (review score, descending)
    path('api/items/games/rating', views.GameListByRating.as_view(), name='games-by-rating-api'), 
    #show specific game
    path('api/items/games/<int:pk>', views.GameDetail.as_view(), name='game-detail-api'),
    
    #get all movies (a-z)
    path('api/items/movies', views.MovieList.as_view(), name='movie-list-api'),
    #get all movies (review score, descending)
    path('api/items/movies/rating', views.MovieListByRating.as_view(), name='movies-by-rating-api'), 
    #get specific movie
    path('api/items/movies/<int:pk>', views.MovieDetail.as_view(), name='movie-detail-api'),

    #get all comics (a-z)
    path('api/items/comics', views.ComicList.as_view(), name='comic-list-api'),
    #get all comics (review score, descending)
    path('api/items/comics/rating', views.ComicListByRating.as_view(), name='comics-by-rating-api'), 
    #show specific comic
    path('api/items/comics/<int:pk>', views.ComicDetail.as_view(), name='comic-detail-api'),

    # get all tv shows (a-z)
    path('api/items/shows', views.TVShowList.as_view(), name='tv-show-list-api'),
    # get all tv shows (review score, descending)
    path('api/items/shows/rating', views.TVShowListByRating.as_view(), name='tv-show-by-rating-api'), 
    # get specific tv show
    path('api/items/shows/<int:pk>', views.TVShowDetail.as_view(), name='tv-show-detail-api'),
    
    
    # other filters
    

    
    
    

    
]



