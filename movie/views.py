from django.shortcuts import render, redirect
from .models import *


def catalog(request):
    films = Movie.objects.all()
    return render(request, 'movie/catalog.html', {'films':films})

def movie_details(request, movie_id):
    film = Movie.objects.get(id=movie_id)
    reviwes = MovieReview.objects.filter(movie_id=movie_id).order_by('-created_at')
    return render(request, 'movie/movie_details.html', {'film': film, 'reviwes':reviwes})

def leave_review(request):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        text = request.POST.get('review_text')
        movie_id = request.POST.get('movie_id')
        MovieReview.objects.create(
            author = request.user,
            movie = Movie.objects.get(id=movie_id),
            text = text
        )
        return redirect('movie_details', movie_id=movie_id)
    
def actor_list(request):
    actors = MoviePerson.objects.filter(role=MoviePerson.RoleType.ACTOR)
    return render(request, 'movie/person_list.html', {'persons':actors, 'title':"АКТЕРЫ"})

def director_list(request):
    director = MoviePerson.objects.filter(role=MoviePerson.RoleType.DIRECTOR)
    return render(request, 'movie/person_list.html', {'persons':director, 'title':'РЕЖИССЁРЫ'})

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'movie/genre_list.html', {'genres':genres})





