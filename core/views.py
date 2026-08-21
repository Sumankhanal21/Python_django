from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request,url_value):
    print("............url value........",url_value)
    # return HttpResponse("Suman is my name")
    print("Suman SUcessfully run and fixed error")
    return render(request,"core/home.html")
