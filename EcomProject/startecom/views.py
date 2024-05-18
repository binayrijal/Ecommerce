from django.shortcuts import render,redirect
from items.models import Items,Category
from startecom.forms import SignupForm
from django.contrib.auth import logout

def index(request):
    items=Items.objects.filter(is_sold=False)[0:6]   #it shows only five items matching
    category=Category.objects.all()
    return render(request,'startecom/index.html',
                  {
                   'items':items,
                   'category':category,
                   })                               #this is main home function to call


def contact(request):
    return render(request,'startecom/contact.html')



def signup(request):
    if request.method=='POST':
      form=SignupForm(request.POST)
      if form.is_valid():
          form.save()

          redirect('/login/')
    else:
          form=SignupForm()

    return render(request,'startecom/signup.html',
                  {
                      'form':form,
                  }
                  )

def logout_user(request):
    logout(request)
    return redirect('/login/')
