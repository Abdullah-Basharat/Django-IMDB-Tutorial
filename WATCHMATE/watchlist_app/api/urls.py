from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("stream",StreamPlatformVS,basename="stream")



# urlpatterns = [
#     path("list/",movie_list,name="movie-list"),
#     path("list/<int:pk>",movie_detail,name="movie-detail"),
# ]


urlpatterns = [
    path("list/",WatchListsAV.as_view(),name="movie-list"),
    path("list/<int:pk>",WatchDetailsAV.as_view(),name="movie-detail"),

    # path("stream/",StreamListsAV.as_view(),name="stream"),
    # path("stream/<int:pk>",StreamDetailsAV.as_view(),name="stream-detail"),
    path("",include(router.urls)),

    path("<int:pk>/review/", ReviewListAV.as_view(), name="review"),
    path("<int:pk>/review-create/", ReviewCreateAv.as_view(), name="review-create"),
    path("review/<int:pk>", ReviewDetailAV.as_view(), name="review-detail"),

    # path("review/",ReviewListAV.as_view(),name="review"),
    # path("review/<int:pk>",ReviewDetailAV.as_view(),name="review-detail"),
]