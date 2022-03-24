from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie, Review
from django.shortcuts import get_object_or_404
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
	#return HttpResponse('<h1> welcome to the home page </h1>')
	#return render(request, 'home.html')
	searchTerm = request.GET.get('searchMovie')
	if searchTerm:
		movies = Movie.objects.filter(title__icontains=searchTerm)
	else:
		movies = Movie.objects.all()
	return render(request, 'home.html',{'searchTerm':searchTerm, 'movies':movies})

def about(request):
	return HttpResponse('<h1> this is the about page </h1>')

def signup(request):
	email = request.GET.get('email')
	return render(request, 'signup.html', {'email': email})

def detail(request, movie_id):
	movie = get_object_or_404(Movie,pk=movie_id)
	reviews = Review.objects.filter(movie = movie)
	return render(request, 'detail.html', {'movie':movie, 'reviews':reviews})

@login_required
def createreview(request, movie_id):
	movie = get_object_or_404(Movie,pk=movie_id)
	if request.method == 'GET':
		return render(request, 'createreview.html',{'form':ReviewForm(), 'movie': movie})
	else:
		try:
			form = ReviewForm(request.POST)
			newReview = form.save(commit=False)
			newReview.user = request.user
			newReview.movie = movie
			newReview.save()
			return redirect('detail', newReview.movie.id)
		except ValueError:
			return render(request, 'createreview.html',{'form':ReviewForm(),'error':'bad data passed in'})