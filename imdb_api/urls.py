
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns


from . import views

urlpatterns = [
    path("list/", views.movie_list.as_view(), name="movie_list"),
    path("list/<int:pk>", views.movie_details.as_view(), name="movie_details"),
    path("stream/", views.stream_list.as_view(), name="stream_list"),
    path("stream/<int:pk>", views.stream_details.as_view(), name="stream_details"),
    path("unwatchlist/", views.UNWatchList.as_view(), name = "unwatchlist"),
    
    path("stream/<int:pk>/review/", views.ReviewList.as_view(), name= "ReviewList"),
    path("stream/<int:pk>/review/create", views.ReviewCreate.as_view(), name= "ReviewDetails"),
    path("stream/review/<int:pk>/", views.ReviewDetails.as_view()),
    path('', views.api_root),

]


urlpatterns = format_suffix_patterns(urlpatterns)
