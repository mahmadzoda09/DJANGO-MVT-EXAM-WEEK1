from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name

class Book(models.Model):
    title = models.CharField(max_length=50)
    pages = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    author = models.ForeignKey( Author ,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title