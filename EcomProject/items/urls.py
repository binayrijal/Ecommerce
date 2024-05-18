from django.urls import path 
from items import views

app_name = 'items'

urlpatterns=[
    path('new/',views.new,name="new"),
    path('',views.items,name="items"),
    path('<int:pk>/',views.details,name="details"),
    path('<int:pk>/edit/',views.edit,name="edit"),
    path('<int:pk>/delete/',views.delete,name="delete"), 
]
