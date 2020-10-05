from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib.messages import constants as messages

# Create your views here.
def index(request):
    context = {
        'variable':"this is sent"
    }
    
    return render(request,"index.html",context)
    #return HttpResponse("This is homepage")
def about(request):
    return render(request,"about.html")
    #return HttpResponse("This is About page")
def services(request):
    return render(request,"services.html")
    #return HttpResponse("This is Services page")
def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        contact = Contact(email=email,password=password,address=address,city=city,zip=zip)
        contact.save()
        
    return render(request,"contact.html")
    #return HttpResponse("This is Contact page")

