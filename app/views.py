from django.shortcuts import render

# Create your views here.

def operations(request):
    a={'a':23,'b':54,'c':95}
    return render(request,'operations.html',a)

def oper(request):
    b={'x':123,'y':1234,'z':456}
    return render(request,'oper.html',b)