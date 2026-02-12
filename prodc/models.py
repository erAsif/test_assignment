from django.db import models


class Product(models.Model):
    Category_choice = [
        ("Electronics", "ELECTRONICS"),
        ("Clothing", "CLOTHING"),
        ("Sports", "SPORTS"),
        ("Furniture", "FURNITURE"),
        ("Books", "BOOKS"),
    ]


    
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=Category_choice)
    price = models.FloatField(max_length=10)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.name