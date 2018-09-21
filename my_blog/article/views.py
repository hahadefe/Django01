# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from article.models import article
import datetime
import random 
import string
# Create your views here.
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

def home(request):
    #return HttpResponse("Hello World，Django")
    post_list = article.objects.all()
    return render(request,'list.html',{'articles':post_list})

def detail(request,my_args):
#    return HttpResponse("you are looking at my_args %s."% my_args)
    post = article.objects.all()[int(my_args)]
    str1 = ("title = %s，category = %s，date_time = %s，content = %s"% (post.title,post.category,post.date_time,post.content))
    return HttpResponse(str1)

def test(request):
    return render(request,'test.html',{'current_time':datetime.now()})

def insert(request):
    title = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S');
    category = id_generator()
    content = id_generator()    
    article.objects.create(title=title,category=category,content=content)
    return render(request,'insert.html')
