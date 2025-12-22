from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('display/index.html')
    context = {
        'item_list' : item_list,
    }
    #Data obtained from the database - django takes the templates and combines it with the data obtained from db then it renders an output,currently context is empty
    return HttpResponse(template.render(context,request))

def item(request):
    return HttpResponse('This is an item view')