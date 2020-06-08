from django.shortcuts import render,redirect
from home.models import Contact
from mysite.models import Post
from django.contrib.auth.models import User

# Create your views here.
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
    post = Post.objects.first()
    context = {'post' : post}
    return render(request, 'home/home.html', context)

def contact(request):
    if(request.method=='POST'):
        name = request.POST['name'];
        email = request.POST['email'];
        phone = request.POST['phone'];
        content = request.POST['content'];
        if(len(name)<2 or len(email)<2 or len(phone)<10 or len(content)<2):
            messages.error(request, "Please fill this form Correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,"Your response has been Submitted Successfully. Thank You!")
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def search(request):
    # allpost = Post.objects.all
    query = request.GET['query']
    if(len(query)>50):
        allpost= Post.objects.none()
    else:
        allpostTitle = Post.objects.filter(title__icontains=query)
        allpostContent = Post.objects.filter(content__icontains=query)
        allpost = allpostTitle.union(allpostContent)
    if(allpost.count()==0):
        messages.warning(request, "Your searched item is not present in this blog.")
    else:
        messages.success(request, "We have something for you.")
    params = {'allpost': allpost, 'query' : query}
    return render(request,'home/search.html', params)

def handleSignup(request):
    if request.method=='POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        myuser = User.objects.create_user(username,email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"You have successfully registered in this Blog. Welcome!")
        return redirect('home')
    else:
        return HttpResponse("404 not Found")
