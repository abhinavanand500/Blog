from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blogHome(request):
    return render(request, 'mysite/blog.html')

def blogPost(request , slug):
    return render(request, 'mysite/blogPost.html')