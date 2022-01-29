from django.urls import path
from .views import signin,index,signup,forgot_pass,otpcheck,newpassword,un

urlpatterns = [
    path('signin/',signin,name="signin"),
    path('signup/',signup,name="signup"),
    path('index/',index,name="index"),
    path('forgotpassword/',forgot_pass,name="forgotpassword"),
    path('otpcheck/',otpcheck,name="otpcheck"),
    path('newpassword/',newpassword,name="newpassword"),
    path('un/',un,name="un"),
    # path('logout/',logout,name=logout)
]
