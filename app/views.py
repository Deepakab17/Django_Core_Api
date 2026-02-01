from django.shortcuts import render,redirect
from .models import Player_Serializer as p

# Create your views here.
def landing(req):
    return render (req,'landing.html')

def list(req):
    if req.method =="POST":
        form =p()
        return render (req,'register.html')
    else :
        return render(req,'landing.html')
def details(req):
    if req.method=="POST":
        form=p()
        data=p.objects.create()
        return render(req,'register.html')
    else:
        return render(req,'landing.html')




