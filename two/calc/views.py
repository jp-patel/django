from django.shortcuts import render

# Create your views here.
def calculate(request):
    if request.GET:
        val1 = request.GET['op1']
        val2 = request.GET['op2']
        opt1 = request.GET['a3']

        if opt1 == '+':
            var = float(val1) + float(val2)
            return render(request,'calculate.html',{'ans':var,'val1':val1,'val2':val2})

        elif opt1 == '-':
            var = float(val1) - float(val2)
            return render(request,'calculate.html',{'ans':var,'val1':val1,'val2':val2})

        elif opt1 == '*':
            var = float(val1) * float(val2)
            return render(request,'calculate.html',{'ans':var,'val1':val1,'val2':val2})

        elif opt1 == '/':
            var = float(val1) / float(val2)
            return render(request,'calculate.html',{'ans':var,'val1':val1,'val2':val2, 'opt1':opt1})

    return render(request,'calculate.html')