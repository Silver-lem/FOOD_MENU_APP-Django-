from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    # template = loader.get_template('display/index.html')
    context = {
        'item_list' : item_list,
    }
    #Data obtained from the database - django takes the templates and combines it with the data obtained from db then it renders an output,currently context is empty
    # return HttpResponse(template.render(context,request)) Instead of this we can write...then we can remove the template that stores the loader
    return render(request,'display/index.html',context )
#import render to use this ..using render() is an efficient way of rendering templates

def item(request):
    return HttpResponse('This is an item view')

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item' : item,
    }
    # return HttpResponse("This is the item's Id : %s" %item_id)
    return render(request,'display/detail.html',context)