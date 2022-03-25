from django.shortcuts import render
from .models import Year

def index(request):
    return render(request,'index.html',{'list':Year.objects.all().order_by('-id')})
