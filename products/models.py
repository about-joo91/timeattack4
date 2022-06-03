from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        db_table ='category'
    name = models.CharField(max_length=128)


class Drink(models.Model):
    class Meta:
        db_table = 'drink'
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class ImageModel(models.Model):
    class Meta:
        db_table = 'img_url'
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    url = models.TextField()