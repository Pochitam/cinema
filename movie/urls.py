from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', catalog, name='home'),
    path('movie_details/<int:movie_id>/', movie_details, name='movie_details'),
    path('leave_review/', leave_review, name='leave_review'),
    path('actors/', actor_list, name='actor_list'),
    path('director/', director_list, name='director_list'),
    path('genres/', genre_list, name='genre_list'),

]