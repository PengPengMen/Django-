# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from myauth.forms import UserCreationForm


# Create your views here.
def register(request):
    form1 = UserCreationForm(request.POST)
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    # 验证数据的合法性
    if form1.is_valid():
        # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
        form1.save()

        if redirect_to:
            return redirect(redirect_to)
        else:
            return redirect('/')

    else:
        form = UserCreationForm()


# 渲染模板
# 如果用户正在访问注册页面，则渲染的是一个空的注册表单
# 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
# 将记录用户注册前页面的 redirect_to 传给模板，以维持 next 参数在整个注册流程中的传递
    return render(request, 'users/register.html', context={'form': form, 'next': redirect_to})

