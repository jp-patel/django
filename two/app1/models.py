from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class category(models.Model):
    categoryName = models.CharField(max_length = 20, null = False)
    categoryId = models.AutoField(auto_created = True, primary_key = True, serialize = False)
    categoryImage = models.ImageField(upload_to='pro_img',default='')

    def __str__(self):
        return self.categoryName

class manufacturer(models.Model):
    manufacturer = models.CharField(max_length = 15, null = False)
    manufacturerImage = models.ImageField(upload_to='pro_img',default='')

    def __str__(self):
        return self.manufacturer

class subCategory(models.Model):
    categoryName = models.ForeignKey(category, on_delete = models.CASCADE)
    subCategoryName = models.CharField(max_length = 20, null = False)
    subCategoryId = models.AutoField(auto_created = True, primary_key = True, serialize = False)
    subCategoryImage = models.ImageField(upload_to='pro_img',default='')

    def __str__(self):
        return self.subCategoryName

class product(models.Model):
    productName = models.CharField(max_length = 20, null = False)
    productId = models.AutoField(auto_created = True, primary_key = True, serialize = False)
    category = models.ForeignKey(category, on_delete = models.CASCADE)
    subCategory = models.ForeignKey(subCategory, on_delete = models.CASCADE)
    ratings = models.FloatField(default = 0, validators=[
            MaxValueValidator(5.0),
            MinValueValidator(0.0)
        ])
    prize = models.PositiveIntegerField(default = 0, validators=[
            MaxValueValidator(99999),
            MinValueValidator(0)
        ])
    description = models.TextField(null = True, default = '')
    productImage = models.ImageField(upload_to='pro_img',default='')
    manufacturer = models.ForeignKey(manufacturer, on_delete = models.CASCADE)

    def __str__(self):
        return self.productName