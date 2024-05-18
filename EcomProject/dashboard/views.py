from django.shortcuts import render
from items.models import Items
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    
    items=Items.objects.filter(created_by=request.user)
    return render(request,'dashboard/index.html',{
        'items':items
    })
