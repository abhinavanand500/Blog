from django.shortcuts import render
from home.models import Contact

# Create your views here.
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def contact(request):
    if(request.method=='POST'):
        name = request.POST['name'];
        email = request.POST['email'];
        phone = request.POST['phone'];
        content = request.POST['content'];
        # print(name)
        # print(email)
        # print(phone)
        # print(content)
        if(len(name)<2 or len(email)<2 or len(phone)<10 or len(content)<2):
            messages.error(request, "Please fill this form Correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,"Your response has been Submitted Successfully. Thank You!")


    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')