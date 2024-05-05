from django.db import models
from django.core.exceptions import ValidationError

class Category(models.Model):
    name=models.CharField(max_length=50)
    order=models.IntegerField(default=1)

    def clean(self):
        if self.name=="Home" or self.name=="home":
            raise ValidationError("Home can't be inserted")

    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['order']

class Post(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,unique=True)
    short_description=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.title
    

   
class Course(models.Model):
    name=models.CharField(max_length=50)
    duration=models.DurationField()

    def __str__(self):
        return self.name 