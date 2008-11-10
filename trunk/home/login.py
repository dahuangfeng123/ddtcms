# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth

def login(request):
    #username = request.POST.get('username', None)
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request,user)
        # 转到成功页面
    else:
        pass# 返回错误信息

    if username:
        request.session['username'] = username
        
    username = request.session.get('username', None)
    if username:
        return render_to_response('login.html', {'username':username})
    else:
        return render_to_response('login.html')

def logout(request):
    try:
        auth.logout(request)
        del request.session['username']
    except KeyError:
        pass
    return HttpResponseRedirect("/login/")

