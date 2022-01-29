from django.contrib import admin
from .models import category, manufacturer, subCategory, product

# Register your models here.
admin.site.register(category)
admin.site.register(manufacturer)
admin.site.register(subCategory)
admin.site.register(product)
