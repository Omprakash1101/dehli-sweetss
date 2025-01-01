from django.contrib.auth.models import User

from django.db import models

class Category(models.Model):
    name= models.CharField(max_length=225)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural='Categories'
        
    def __str__(self):
        return self.name
    
class Items(models.Model):
    Category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name=models.CharField(max_length=225)
    img=models.ImageField(upload_to='item_images', blank=True, null=False)
    price=models.FloatField()
    is_sold = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name    
    
    