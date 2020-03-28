from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

    def to_category_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.TextField(default='')
    count = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def to_product_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'category_id': self.category_id.to_category_json()
        }