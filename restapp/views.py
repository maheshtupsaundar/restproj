from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.
def myview(request):
    qs=Product.objects.all()
    ps1=ProductSerializer(qs,many=True)
    jr1=JSONRenderer()
    res1=jr1.render(ps1.data)
    return HttpResponse(res1,content_type="application/json")
def input(request):
    return render(request,'input.html')
def insert(request):
    v1=int(request.GET["t1"])
    v2=request.GET["t2"]
    v3=float(request.GET["t3"])
    v4=request.GET["t4"]
    v5=request.GET["t5"]
    p1=Product(v1,v2,v3,v4,v5)
    p1.save()
    return render(request,'input.html')
