from django.shortcuts import render, redirect
from django.http import HttpResponse
from mysite.models import Post, BlogComment
from django.contrib import messages
from mysite.templatetags import getDict
# Create your views here.
def blogHome(request):
    allPost = Post.objects.all().reverse()
    print(allPost)
    allPost.reverse()
    print(allPost)
    context = {'allPost': allPost}
    return render(request, 'mysite/blog.html', context)

def blogPost(request , slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    repDict={}
    for reply in replies:
        if reply.parent.sno not in repDict.keys():
            repDict[reply.parent.sno] = [reply]
        else:
            repDict[reply.parent.sno].append(reply)

        print(repDict)
    context = {'post':post, 'comments':comments , 'user' : request.user, 'replyDict' : repDict}
    return render(request, 'mysite/blogPost.html',context)

def postComment(request):
    if request.method=="POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno = postSno)
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your Comment has been posted Successfully")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post, parent = parent)
            comment.save()
            messages.success(request, "Your reply has been posted Successfully")

    return redirect(f'/blog/{post.slug}')