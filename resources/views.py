from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def resources(request):
    return HttpResponse("<h1>Resources</h1>")

def django(request):
    return HttpResponse("<h1>django</h1>")

def blog(request):
    return render(request, 'resources/blog.html')