from django.urls import path, include 
from . import views


# I included paths for both requesting pure json responses (api) AND for viewing the data in a browser view

app_name = 'media'


urlpatterns = [
    path('', views.masterIndex, name='master_index'),
    path('api/items', views.MediaList.as_view(), name='master_index_api'),
    
    path('<int:id>/', views.masterDetail, name='master_detail'),
    path('api/items/<int:pk>/', views.MediaDetail.as_view(), name='master_detail_api'),
    
    path('api/items/games', views.GameList.as_view(), name='game-list'),
    path('api/items/games/<int:pk>', views.GameDetail.as_view(), name='game-detail'),
    
    path('api/items/movies', views.MovieList.as_view(), name='movie-list'),
    path('api/items/movies/<int:pk>', views.MovieDetail.as_view(), name='movie-detail'),

    path('api/items/comics', views.ComicList.as_view(), name='comic-list'),
    path('api/items/comics/<int:pk>', views.ComicDetail.as_view(), name='comic-detail'),

    path('api/items/shows', views.ShowList.as_view(), name='show-list'),
    path('api/items/shows/<int:pk>', views.ShowDetail.as_view(), name='show-detail'),
    
]



