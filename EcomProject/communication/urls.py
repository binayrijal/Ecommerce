from django.urls import path
from communication.views import new_communication,inbox


app_name='communication'

urlpatterns=[
    path('',inbox,name="inbox"),
    path('new/<int:item_pk>/',new_communication,name="newcommunication")
]