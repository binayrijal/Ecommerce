from django.db import models
from items.models import Items
from django.contrib.auth.models import User

# Create your models here.
class Communication(models.Model):
    com_item=models.ForeignKey(Items,related_name='communications',on_delete=models.CASCADE)
    members=models.ManyToManyField(User,related_name='communications')
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering= ('-modified_at',)

    

class CommunicationMessage(models.Model):
    communication=models.ForeignKey(Communication,related_name='message',on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name='created_message',on_delete=models.CASCADE)

   