# from django.db import models
# from django.core.validators import MaxValueValidator, MinValueValidator

# # Create your models here.
# class category(models.Model):
#     categoryName = models.CharField(max_length = 20, null = False)
#     categoryId = models.AutoField(auto_created = True, primary_key = True, serialize = False)
#     categoryImage = models.ImageField(upload_to='pro_img',default='')

#     def __str__(self):
#         return self.categoryName