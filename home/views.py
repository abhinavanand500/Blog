from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def contact(request):
    return HttpResponse('This is Contact')

def about(request):
    return HttpResponse('This is About')