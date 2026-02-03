from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Player_Serializer as p
import json
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def landing(req):
    return render (req,'landing.html')
@csrf_exempt
def player_list(req):
    if req.method =="POST":
        j_data=req.body
        print(j_data)
        print(type(j_data))
        p_data=json.loads(j_data)
        print(p_data)
        print(type(p_data))
        n=p_data.get('name')
        a=p_data.get('age')
        c=p_data.get('country')
        j=p_data.get('jersy_number')
        if 'name' in p_data and 'age' in p_data and 'country' in p_data and 'jersy_number' in p_data:
            p.objects.create(name=n,age=a,country=c,jersy_number=j)
            d={
                'msg':'Object created successfully'
            }
            j_data=json.dumps(d)
            return HttpResponse(j_data,content_type='application/json')
        else:
            d={
                'msg':'Some required feilds are not found'
            }
            j_data=json.dumps(d)
            return HttpResponse(j_data,content_type='application/json')

    data=p.objects.all().values()
    print(data)
    p_data=list(data)
    print(p_data)
    j_data=json.dumps(p_data)
    return HttpResponse(j_data,content_type='application/json')
@csrf_exempt
def details(req,id):
    if req.method =="PUT":
        j_data=req.body
        print(j_data)
        print(type(j_data))
        p_data=json.loads(j_data)
        print(p_data)
        print(type(p_data))
        if 'name' in p_data and 'age' in p_data and 'country' in p_data and 'jersy_number' in p_data:
            old_data=p.objects.get(id=id)
            old_data.name=p_data.get('name')
            old_data.age=p_data.get('age')
            old_data.country=p_data.get('country')
            old_data.jersy_number=p_data.get('jersy_number')
            old_data.save()
            d={"message":"Object updated "}
            j_data=json.dumps(d)
            return HttpResponse(j_data,content_type='application/json')
    if req.method == "PATCH":
        j_data = req.body
        print(j_data)
        print(type(j_data))

        p_data = json.loads(j_data)
        print(p_data)
        print(type(p_data))
        old_data = p.objects.get(id=id)
        if 'name' in p_data:
            old_data.name = p_data.get('name')
        if 'age' in p_data:
            old_data.age = p_data.get('age')
        if 'country' in p_data:
            old_data.country = p_data.get('country')
        if 'jersy_number' in p_data:
            old_data.jersy_number = p_data.get('jersy_number')
        old_data.save()
        d = {"d": "object updated in parts"}
        j_data=json.dumps(d)
        return HttpResponse(
            j_data,
            content_type='application/json'
        )

    

    data=p.objects.get(id=id)
    print(data)
    p_data=model_to_dict(data)
    # print(p_data)
    # j_data=json.dumps(p_data)
    return JsonResponse(p_data,safe=False)

