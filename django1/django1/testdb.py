# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test

def testdb(request):
    test1 = Test(name='djangosql')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")