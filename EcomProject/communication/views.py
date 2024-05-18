from django.shortcuts import render,get_object_or_404,redirect
from items.models import Items
from .models import CommunicationMessage,Communication
from .forms import CommunicationMessageForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def new_communication(request,item_pk):
    item=get_object_or_404(Items,pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')
        
    communications=Communication.objects.filter(com_item=item).filter(members__in=[request.user.id])

    if communications:
        pass

    if request.method=='POST':
        form=CommunicationMessageForm(request.POST)
        
        if form.is_valid():
            communication=Communication.objects.create(com_item=item)
            communication.members.add(request.user)
            communication.members.add(item.created_by)
            communication.save()

            communication_message=form.save(commit=False)
            communication_message.communication=communication
            communication_message.created_by=request.user
            communication_message.save()

            return redirect ('items:details', pk=item_pk)
    else:
        form=CommunicationMessageForm()

    return render(request,'communication/new.html',{
        
        'form':form,
    })



@login_required
def inbox(request):
   communications=Communication.objects.filter(members__in=[request.user.id])

  
   return render(request,'communication/inbox.html',{
       'communications':communications,
   })