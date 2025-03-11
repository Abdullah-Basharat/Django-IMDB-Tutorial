from django.http import JsonResponse
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer
from rest_framework.decorators import api_view
from ..models import WatchList, StreamPlatform, Review
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

from rest_framework import viewsets
from .permission import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated



# Create your views here.
# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = WatchList.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request, pk):
#     try:
#         movie = WatchList.objects.get(pk=pk)
#     except WatchList.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#
#     if request.method == 'PUT':
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == 'DELETE':
#         WatchList.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ReviewListAV(mixins.ListModelMixin,
#                  mixins.CreateModelMixin,
#                  generics.GenericAPIView):
#
#     serializer_class = ReviewSerializer
#     queryset = Review.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
# class ReviewDetailAV(mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin,
#                      generics.GenericAPIView):
#     serializer_class = ReviewSerializer
#     queryset = Review.objects.all()
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#

class ReviewListAV(generics.ListAPIView):

    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        watchlist = self.kwargs['pk']
        return Review.objects.filter(movie=watchlist)


class ReviewDetailAV(generics.RetrieveUpdateDestroyAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class ReviewCreateAv(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watchlist = WatchList.objects.get(pk=pk)
        review_user = self.request.user
        review_query = Review.objects.filter(movie=watchlist,reviewer=review_user)

        if review_query.exists():
            raise ValidationError("You are already reviewed")
        serializer.save(movie=watchlist,user=review_user)

class StreamPlatformVS(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(user)
        return Response(serializer.data)

# class StreamListsAV(APIView):
#
#     def get(self,request):
#         platform = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(platform, many=True,context={'request': request})
#         return Response(serializer.data)
#
#     def post(self,request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)\
#
# class StreamDetailsAV(APIView):
#     def get(self,request,pk):
#         try:
#             platform = StreamPlatform.objects.get(pk=pk)
#             serializer = StreamPlatformSerializer(platform,context={'request': request})
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except StreamPlatform.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#
#     def put(self,request,pk):
#         try:
#             platform = StreamPlatform.objects.get(pk=pk)
#             serializer = StreamPlatformSerializer(platform, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#         except StreamPlatform.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def delete(self,request,pk):
#         try:
#             platform = StreamPlatform.objects.get(pk=pk)
#             platform.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except StreamPlatform.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

class WatchListsAV(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WatchDetailsAV(APIView):

    def get(self,request,pk):
        try:
            movie = WatchList.objects.get(pk=pk)
            serializer = WatchListSerializer(movie)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except WatchList.DoesNotExist:
            return Response({"Error":"Movie Not Found"},status=status.HTTP_404_NOT_FOUND)



    def put(self,request,pk):
        try:
            movie = WatchList.objects.get(pk=pk)
            serializer = WatchListSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except WatchList.DoesNotExist:
            return Response({"Error":"Movie Not Found"},status=status.HTTP_404_NOT_FOUND)


    def delete(self,request,pk):
        try:
            movie = WatchList.objects.get(pk=pk)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except WatchList.DoesNotExist:
            return Response({"Error":"Movie Not Found"},status=status.HTTP_404_NOT_FOUND)
