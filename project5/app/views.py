from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.


def register(request):
    if request.method == 'POST':
        name = request.POST.get('nme')
        pno = request.POST.get('pno')
        email = request.POST.get('email')
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        emp = Emp(name=name, pno=pno, email=email, username=un, pw=pw)
        emp.save()
        return HttpResponse('Registered Successfull')

    return render(request, 'register.html')