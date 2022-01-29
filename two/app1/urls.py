from django.urls import path
from .views import index,getdata,home,submit,categories,subcategories,products,manufacturers,productdetails,about,categorySubmit,subCategorySubmit,productSubmit,manufacturerSubmit#,submitdata
from django.conf import settings
from django.conf.urls.static import static
from Login.views import signin, logout

urlpatterns = [
    path('', index),
    path('g/', getdata, name = 'getdata'),
    # path('s/', submitdata, name = 'submitdata'),
    path('home/', home, name = 'home'),
    path('submit/', submit, name = 'submit'),
    path('categories/', categories, name = 'categories'),
    path('subcategories/', subcategories, name = 'subcategories'),
    path('products/', products, name = 'products'),
    path('manufacturers/', manufacturers, name = 'manufacturers'),
    path('productdetails/<int:pk>', productdetails , name = 'productdetails'),
    path('categorySubmit/', categorySubmit, name = 'categorySubmit'),
    path('subCategorySubmit/', subCategorySubmit, name = 'subcategorySubmit'),
    path('productSubmit/', productSubmit, name = 'productSubmit'),
    path('manufacturerSubmit/', manufacturerSubmit, name = 'manufacturerSubmit'),
    path('about/', about, name = 'about'),
    path('signin/', signin , name = 'signin'),
    path('logout/', logout , name = 'logout')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)