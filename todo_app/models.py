from django.db import models


class Category(models.Model):
    category_type = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_type

class Todolist(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length = 200)
    image = models.ImageField(upload_to='images/', blank=True, max_length=200)
    completed = models.BooleanField(default=False)



    