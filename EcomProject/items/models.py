from typing import Any
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=200)

    class Meta:
        ordering=('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Items(models.Model):
    Category=models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    description=models.TextField(blank=True, null=True)
    price=models.IntegerField()
    image=models.ImageField(upload_to='items_pic',blank=True,null=True)
    is_sold=models.BooleanField(default=False)
    created_by=models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
