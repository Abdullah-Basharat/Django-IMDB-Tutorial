from django.urls import path
from .views import *


# urlpatterns = [
#     path("list/",movie_list,name="movie-list"),
#     path("list/<int:pk>",movie_detail,name="movie-detail"),
# ]


urlpatterns = [
    path("list/",WatchListsAV.as_view(),name="movie-list"),
    path("list/<int:pk>",WatchDetailsAV.as_view(),name="movie-detail"),

    path("stream/",StreamListsAV.as_view(),name="stream"),
    path("stream/<int:pk>",StreamDetailsAV.as_view(),name="stream-detail"),

    path("stream/<int:pk>/review/", ReviewListAV.as_view(), name="review"),
    path("stream/<int:pk>/review-create/", ReviewCreateAv.as_view(), name="review-create"),
    path("stream/review/<int:pk>", ReviewDetailAV.as_view(), name="review-detail"),

    # path("review/",ReviewListAV.as_view(),name="review"),
    # path("review/<int:pk>",ReviewDetailAV.as_view(),name="review-detail"),
]