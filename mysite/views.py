from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Post
# Create your views here.
def blogHome(request):
    allPost = Post.objects.all()
    context = {'allPost': allPost}
    return render(request, 'mysite/blog.html', context)

def blogPost(request , slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request, 'mysite/blogPost.html',context)