from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, JsonResponse
from .models import WatchList, StreamPlatform, UNWatchList, Review
from .serializers import WatchListSerializers, StreamPlatformSerializers, ReviewSerializers ,UNWatchListSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.views import APIView

from rest_framework.serializers import ValidationError

from rest_framework import mixins
from rest_framework import generics

from rest_framework.reverse import reverse
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'movie_list': reverse('movie_list', request=request, format=format),
        'stream_list': reverse('stream_list', request=request, format=format)
    })


class stream_list(generics.ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializers
    
class stream_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializers
    
    
class movie_list(generics.ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializers
    

class movie_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializers
    

class ReviewList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    
    def get_queryset(self):
        pk = self.kwargs['pk'] 
        return Review.objects.filter(watchlist = pk)
    

class ReviewCreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        movie = WatchList.objects.get(pk= pk)
        review_user = self.request.user
        review_queryset = Review.objects.filter(review_user = review_user, watchlist= movie)
        if review_queryset:
            raise ValidationError(" You Can't Review Multiple Time ")            
        serializer.save(watchlist= movie, review_user = review_user)
        

class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    
  
class UNWatchList(generics.ListCreateAPIView):
    queryset = UNWatchList.objects.all()
    serializer_class = UNWatchListSerializers
    
    
#====================================================================================================================================

# class stream_list(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializers
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class stream_details(mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin,
#                      generics.GenericAPIView):
    
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializers
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
    
    
#====================================================================================================================================================
#===================================================================================================================================================

# class stream_list(APIView):
    
#     def get(self, request):
#         stream = StreamPlatform.objects.all()
#         serialized= StreamPlatformSerializers(stream, many= True)
#         return Response(serialized.data)
#     def post(self, request):
#         _data = request.data
#         serialized = StreamPlatformSerializers(data= _data, many= True)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status=status.HTTP_201_CREATED)
#         return Response(serialized.data, status=status.HTTP_400_BAD_REQUEST)


# class stream_details(APIView):
#     def get_object(self, pk):
#         try:
#             return StreamPlatform.objects.get(pk= pk)
#         except StreamPlatform.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         stream_detail = self.get_object(pk= pk)
#         serialized = StreamPlatformSerializers(stream_detail)
#         return Response(serialized.data)
    
#     def put(self, request, pk):
#         stream_detail = self.get_object(pk)
#         serialized = StreamPlatformSerializers(stream_detail, data= request.data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data)
#         return Response(serialized.errors, status = status.HTTP_404_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         stream_detail = self.get_object(pk)
#         stream_detail.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

    
        
#==============================================================================================================================================================================================
        
# Create your views here.


# @api_view(["GET"])
# def movie_list(request):
#     movie_list = WatchList.objects.all()
#     serialized = WatchListSerializers(movie_list, many= True)
#     print(movie_list)
#     return Response(serialized.data)



# @api_view(['GET'])
# def movie_details(request, pk):
#     movie = WatchList.objects.get(pk=pk)
#     serialized = WatchListSerializers(movie)
#     print(serialized)
#     return Response(serialized.data)


# @api_view(['GET', 'POST'])
# def stream_list(request):
    
#     if request.method == "GET":
#         stream = StreamPlatform.objects.all()
#         serialized = StreamPlatformSerializers(stream, many= True)
#         # print(serialized.data)
#         return Response(serialized.data)
#     elif request.method == "POST":
#         _data= request.data
#         print(_data)
#         serialized = StreamPlatformSerializers(data=_data, many= True)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data, status = status.HTTP_201_CREATED)
#         return Response(serialized.data, status=status.HTTP_400_BAD_REQUEST)
        

# @api_view(['GET', 'PUT', 'DELETE'])
# def stream_details(request, pk, format= None ):
    
#     try: 
#         stream_details = StreamPlatform.objects.get(pk=pk)
#     except stream_details.DoesNotExist:  
#         return Response(status=status.HTTP_404_NOT_FOUND)  
    
#     if request.method == "GET":
#         serialized = StreamPlatformSerializers(stream_details)
#         return Response(serialized.data)
    
#     elif request.method == "PUT":
#         _data = request.data
#         serialized = StreamPlatformSerializers(stream_details, data= _data)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data)
#         return Response(serialized.errors, status= status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == "DELETE":
#         stream_details.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        

    