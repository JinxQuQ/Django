from django.http import HttpResponse
from django.shortcuts import render
import datetime

def runoob(request):
    # context = {}
    # context['hello'] = 'Hello, world'
    views = ["hello","bye"]
    timenow = datetime.datetime.now()
    links = "<a href='https://www.runoob.com/django/django-template.html'>点击跳转</a>"
    view_dict = {"name": "lihui", "age": "23","sex": "female"}
    num1 = 88
    num2 = 128
    return render(request,'runoob.html',{'name':timenow, 'views':views,'links':links,'view_dict':view_dict,'num1':num1,'num2':num2})

    # return render(request,'runoob.html',{'num1':num1})
def other(request):
    num1 = 88
    return render(request, 'other.html',{'num1':num1})
# def hello(request):
#     return HttpResponse('Hello')

