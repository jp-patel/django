from django.shortcuts import render,redirect
from django.http import request,HttpResponseRedirect,HttpResponse
from .models import Member
from .forms import MemberForm
import random
# from practice.decorator import status

# @status
def signin(request):
    if request.method=="POST":
        try:
            m = Member.objects.get(username=request.POST['username'])
            if m.password == request.POST['password']:
                request.session['username'] = m.username
                return HttpResponseRedirect('/home')
            else:
                return HttpResponse("<h2><a href=''>You have entered wrong password </a></h2>")
        except:
            return HttpResponse("<h2><a href=''>No username found.</a></h2>")
    return render(request,'signin.html')

# def forgot_pass(request):
#     return render(request,'forgotpassword.html')

def forgot_pass(request):
    if request.method=='POST':
        user = request.POST.get('username')
        if user == None:
            return render(request,'forgotpassword.html')
        otp=generate_otp(request)
        print(otp)
        request.session['otp'] = otp
        request.session['username'] = user
        return redirect('otpcheck')
    return render(request,'forgotpassword.html')

def otpcheck(request):
    if request.session.has_key('otp'):
        otp = request.session['otp']
        try:
            otpobj = request.POST.get('otp')
            if otpobj == None:
                return render(request,'otp.html')
            if otp == request.POST.get('otp'):
                return redirect('newpassword')
            else:
                return HttpResponse("<a href = ''> Wrong otp entered.</a>")
        except:
            return redirect('signin')
    return render(request,'otp.html')

def newpassword(request):
    if request.session.has_key('username'):
        new_pass = request.POST.get('password')
        if new_pass == None:
            return render(request,'newpassword.html')
        obj = Member.objects.get(username = request.session['username'])
        obj.password = new_pass
        obj.save()
        return redirect('signin')
    else:
        return redirect('signin')
    return render(request,'newpassword.html')

def logout(request):
    if request.session.has_key('username'):
        del request.session['username']
    return redirect('signin')

def index(request):
    if request.session.has_key('username'):
        return render(request,'index.html')
    else:
        return redirect('signin')

def signup(request):
    obj=MemberForm(request.POST)
    if obj.is_valid():
        obj.save()
    return render(request,'signup.html',{'obj':obj})

def un(request):
    return render(request,'Un.html')

def generate_otp(request):
    otp=''
    otp = otp + random.choice('0123456789')
    otp = otp + random.choice('0123456789')
    otp = otp + random.choice('0123456789')
    otp = otp + random.choice('0123456789')
    otp = otp + random.choice('0123456789')
    otp = otp + random.choice('0123456789')
    return otp