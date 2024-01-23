from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "Static1/index.html")
def add(request):
    return render(request, "Static1/form.html") 
