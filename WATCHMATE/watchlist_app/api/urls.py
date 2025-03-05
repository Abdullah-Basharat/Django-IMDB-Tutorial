from django.urls import path
from .views import *


# urlpatterns = [
#     path("list/",movie_list,name="movie-list"),
#     path("list/<int:pk>",movie_detail,name="movie-detail"),
# ]


urlpatterns = [
    path("list/",MovieList.as_view(),name="movie-list"),
    path("list/<int:pk>",MovieDetail.as_view(),name="movie-detail"),
]