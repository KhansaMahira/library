from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    author = models.TextField()
    publisher = models.TextField()
    book_category = models.TextField()
    isbn = models.TextField()