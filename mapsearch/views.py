from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def map_search(request):
    return render(request, 'mapsearch.html')