from django.shortcuts import render, HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("Welcome to django course")

def index(request):
    return render(request, "index.html")
