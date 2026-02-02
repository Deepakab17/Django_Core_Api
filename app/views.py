from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Player_Serializer as p
import json
from django.forms.models import model_to_dict

# Create your views here.
def landing(req):
    return render (req,'landing.html')

def player_list(req):
    # if req.method =="POST":
    #     form =p()
    #     return render (req,'register.html')
    # else :
    #     return render(req,'landing.html')
    data=p.objects.all().values()
    print(data)
    p_data=list(data)
    print(p_data)
    j_data=json.dumps(p_data)
    return HttpResponse(j_data,content_type='application/json')

def details(req,id):
    # if req.method=="POST":
    #     form=p()
    #     data=p.objects.create()
    #     return render(req,'register.html')
    # else:
    #     return render(req,'landing.html')
    data=p.objects.get(id=id)
    print(data)
    p_data=model_to_dict(data)
    # print(p_data)
    # j_data=json.dumps(p_data)
    return JsonResponse(p_data,safe=False)

