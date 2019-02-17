from django.shortcuts import render

def index(request):
    render(request, 'listings/listing.html')
