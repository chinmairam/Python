from django.db import models

class Store(models.Model):
    store_name = models.CharField(max_length=50)
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=30)
    def __str__(self):
        return self.store_name + ", " + self.state + ", " + self.country

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    brand = models.CharField(max_length=40)
    category = models.CharField(max_length=30)
    def __str__(self):
        return self.product_name + ", " + self.brand + ", " +self.category
    
class Sales(models.Model):
    date = model.DateField()
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    units_sold = models.IntegerField(default=0)
    def __str__(self):
        return str(self.date) + ", " + str(self.store_id) + ", " + str(self.product_id)+", "+str(self.units_sold)

    
