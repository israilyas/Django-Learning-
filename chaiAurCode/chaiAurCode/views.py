from django.http import HttpResponse
from django.shortcuts import render

# HttpResponse By importing it we can take request and Response

def home(request):
    # return HttpResponse("Hello World, You are at Chai aur Django Home")
    return render(request,'index.html')

def about(request):
    # return HttpResponse("Hello World, You are at Chai aur Django About")
    return render(request,'about.html')

def contact(request):
    # return HttpResponse("Hello World, You are at Chai aur Django Contact")
    return render(request,'contact.html')