from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


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