from django.shortcuts import render,HttpResponse
import datetime
from .models import housemodule
from project51app1.models import housemodule
# Create your views here.
def home(request):
    content = {}
    content['dataset'] = housemodule.objects.all()
    return render(request,'webtech.html',content)
