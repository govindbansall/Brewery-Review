from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('search')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('search')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



import requests
from django.shortcuts import render, get_object_or_404
from .models import Brewery, Review

BREWERY_API_URL = 'https://api.openbrewerydb.org/breweries'

def search_view(request):
    query = request.GET.get('query')
    search_by = request.GET.get('search_by', 'city')
    breweries = []

    if query:
        response = requests.get(f'{BREWERY_API_URL}?by_{search_by}={query}')
        if response.status_code == 200:
            breweries = response.json()

    return render(request, 'search.html', {'breweries': breweries})

def brewery_detail_view(request, brewery_id):
    brewery = get_object_or_404(Brewery, id=brewery_id)
    reviews = Review.objects.filter(brewery=brewery)
    return render(request, 'brewery_detail.html', {'brewery': brewery, 'reviews': reviews})

def add_review_view(request, brewery_id):
    if request.method == 'POST':
        rating = request.POST['rating']
        description = request.POST['description']
        brewery = get_object_or_404(Brewery, id=brewery_id)
        Review.objects.create(
            user=request.user,
            brewery=brewery,
            rating=rating,
            description=description
        )
        return redirect('brewery_detail', brewery_id=brewery_id)
    return redirect('brewery_detail', brewery_id=brewery_id)