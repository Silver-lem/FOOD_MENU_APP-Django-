from django.urls import path
from . import views

app_name = 'display'
urlpatterns = [
    #/display/
    path('',views.index,name='index'),
    #/display/id
    path('<int:item_id>/',views.detail,name ='detail'),
    path('item/',views.item,name='item'),
]