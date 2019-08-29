from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Category
from .forms import CategoryForm
import json

# Create your views here.
def categorym(request):
    items=Category.objects.all()
    context = {
            'items':items 
    }
    return render(request,'base.html',context=context)





def categorys(request):
   
    if request.method == 'GET':
        form = CategoryForm()    
    else:
        form = CategoryForm(request.POST)
        # print(form.is_valid())
        if form.is_valid():
           
           title = form.cleaned_data['title']
           url = form.cleaned_data['url']
           description = form.cleaned_data['description']
           parentid = form.cleaned_data['parentid']
           summary = form.cleaned_data['summary']
           Category.objects.create(title=title,url=url,description=description,parentid=parentid,summary=summary)
           
    return render(request, "success.html", {'form': form})

def success(request):
    data=Category.objects.all()
    context = {
            'data':data 
    }
    return render(request,'abc.html',context=context)


def parentt(request,id):    
    dataa=Category.objects.filter(parentid=id)
    
    context = {
            'dataa':dataa 
    }
    return render(request,'parentt.html',context=context)