from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context ={
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'service.html')

def contact(request):
    return render(request,'contact.html')