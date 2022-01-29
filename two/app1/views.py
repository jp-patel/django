from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import category,subCategory,product,manufacturer
from .forms import categoryForm,subCategoryForm,manufacturerForm,productForm

# Create your views here.
def index(request):
    return  HttpResponse("Welcome to the index page.")

def getdata(request):
    categoryObject = category.objects.all()
    subCategoryObject = subCategory.objects.all()
    productObject = product.objects.all()
    manufacturerObject = manufacturer.objects.all()
    return render(request,'index.html',{'category':categoryObject,'subCategory':subCategoryObject,'product':productObject,'manufacturer':manufacturerObject})

# def submitdata(request):
#     Submit = productForm(request.POST)
#     if Submit.is_valid():
#         Submit.save()
#     return render(request, 'submit.html', {'data' : Submit})

def home(request):
    if request.session.has_key("username"):
        return render(request,'index.html',{'home':True})
    else:
        return redirect('signin')

def submit(request):
    if request.session.has_key('username'):
        return render(request,'submit.html',{'submit':True})
    else:
        return redirect('signin')

def categories(request):
    if request.session.has_key('username'):
        categoryObject = category.objects.all()
        return render(request,'index.html',{'category':categoryObject})
    else:
        return redirect('signin')

def subcategories(request):
    if request.session.has_key('username'):
        subCategoryObject = subCategory.objects.all()
        return render(request,'index.html',{'subCategory':subCategoryObject})
    else:
        return redirect('signin')

def products(request):
    if request.session.has_key('username'):
        productObject = product.objects.all()
        return render(request,'index.html',{'product':productObject})
    else:
        return redirect('signin')

def manufacturers(request):
    if request.session.has_key('username'):
        manufacturerObject = manufacturer.objects.all()
        return render(request,'index.html',{'manufacturer':manufacturerObject})
    else:
        return redirect('signin')

# code to call a product with name
# def productdetails(request):
#     if request.method == 'GET':
#         productname = request.GET.get('product',None)
#         productDetailObject = product.objects.get(productName=productname)
#         return render(request,'index.html',{'productDetail':productDetailObject})

# code to call a product with id
def productdetails(request, pk):
    if request.session.has_key('username'):
        productDetailObject = get_object_or_404(product, pk=pk)
        return render(request,'index.html',{'productDetail':productDetailObject})
    else:
        return redirect('signin')

def categorySubmit(request):
    if request.session.has_key('username'):
        categorySubmitObject = categoryForm(request.POST)
        if categorySubmitObject.is_valid():
            categorySubmitObject.save()
            categorySubmitObject = categoryForm()
        return render(request, 'submit.html', {'category' : categorySubmitObject})
    else:
        return redirect('signin')

def manufacturerSubmit(request):
    if request.session.has_key('username'):
        manufacturerSubmitObject = manufacturerForm(request.POST)
        if manufacturerSubmitObject.is_valid():
            manufacturerSubmitObject.save()
            manufacturerSubmitObject = manufacturerForm()
        return render(request, 'submit.html', {'manufacturer' : manufacturerSubmitObject})
    else:
        return redirect('signin')

def subCategorySubmit(request):
    if request.session.has_key('username'):
        subCategorySubmitObject = subCategoryForm(request.POST)
        if subCategorySubmitObject.is_valid():
            subCategorySubmitObject.save()
            subCategorySubmitObject = subCategoryForm()
        return render(request, 'submit.html', {'subCategory' : subCategorySubmitObject})
    else:
        return redirect('signin')

def productSubmit(request):
    if request.session.has_key('username'):
        productSubmitObject = productForm(request.POST)
        if productSubmitObject.is_valid():
            productSubmitObject.save()
            productSubmitObject = productForm()
        return render(request, 'submit.html', {'product' : productSubmitObject})
    else:
        return redirect('signin')

def about(request):
    if request.session.has_key('username'):
        return render(request,'about.html')
    else:
        return redirect('signin')
