from django.shortcuts import render, redirect
from django.http import HttpResponse
from mysite.models import Post, BlogComment
from django.contrib import messages

# Create your views here.
def blogHome(request):
    allPost = Post.objects.all()
    context = {'allPost': allPost}
    return render(request, 'mysite/blog.html', context)

def blogPost(request , slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post)
    context = {'post':post, 'comments':comments}
    return render(request, 'mysite/blogPost.html',context)

def postComment(request):
    if request.method=="POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno = postSno)
        comment = BlogComment(comment=comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your Comment has been posted Successfully")

    return redirect(f'/blog/{post.slug}')