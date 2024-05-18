from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Items,Category
from items.forms import NewItemForm,EditItemForm
from django.shortcuts import redirect
from django.db.models import Q


def items(request):
    query=request.GET.get('query','')
    category_id=request.GET.get('category', 0)
    category=Category.objects.all()
    search_item=Items.objects.filter(is_sold=False)

    if category_id:
        search_item=search_item.filter(Category_id=category_id)
    
    if query:
        search_item=search_item.filter(Q(name__icontains=query) | Q(description__icontains=query))

    
    
    return render(request,'items/items.html',{
        'search_item':search_item,
        'query':query,
        'category':category,
        'category_id':int(category_id)
    })

def details(request,pk):
    items=get_object_or_404(Items,pk=pk)
    related_items=Items.objects.filter(Category=items.Category,is_sold=False).exclude(pk=pk)
    return render(request,'items/detail.html',
    {
     'items':items,
     'related_items':related_items
    }
    )

@login_required
def new(request):
    if request.method=="POST":
        form=NewItemForm(request.POST,request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect('items:details', pk=item.id)
    else:
        form=NewItemForm()
    return render(request,'items/form.html',{
      'form':form, 
      'title':'New item',
 
   })


@login_required
def edit(request,pk):
    items=get_object_or_404(Items,pk=pk,created_by=request.user)
    if request.method=="POST":

        form=EditItemForm(request.POST,request.FILES,instance=items)
        if form.is_valid():
            form.save()
            return redirect('items:details', pk=pk)
    else:

        form=EditItemForm(instance=items)


    return render(request,'items/form.html',{
      'form':form, 
      'title':'Edit item',
 
   }) 
    




@login_required
def delete(request,pk):

    items=get_object_or_404(Items,pk=pk,created_by=request.user)
    items.delete()
    return redirect('dashboard:index')

