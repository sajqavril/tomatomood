from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def background_investigation(request):
    return render(request, 'background_investigation.html')

def product_design(request):
    return render(request, 'product_design.html')

def continuous_meaning(request):
    try:
        return render(request, 'continuous_meaning.html')  
    except:
        return render(request, 'no-sidebar.html')  

def tech_support(request):
    try:
        return render(request, 'tech_support.html')   
    except:
        return render(request, 'left-sidebar.html')   

def homework_echarts(request):
    return render(request, 'homework.html')

def product_echarts(request):
    return render(request, 'product.html')