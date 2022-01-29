from django import forms
from .models import category,manufacturer,subCategory,product

class categoryForm(forms.ModelForm):
    class Meta:
        model=category
        fields=['categoryName', ]#'categoryImage']

class manufacturerForm(forms.ModelForm):
    class Meta:
        model=manufacturer
        fields=['manufacturer', ]#'manufacturerImage']

class subCategoryForm(forms.ModelForm):
    class Meta:
        model=subCategory
        fields=['categoryName', 'subCategoryName', ]#'subCategoryImage']

class productForm(forms.ModelForm):
    class Meta:
        model=product
        fields=['productName', 'category', 'subCategory', 'ratings', 'prize', 'description', 'manufacturer', ]#'productImage', 'manufacturer']


#0101010100010101010
#0111010101010100101
