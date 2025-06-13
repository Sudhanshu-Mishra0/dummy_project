from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    """
    Render the home page.
    """
    return HttpResponse("Hello, world! This is the home page of the base app.")