import json
from django.shortcuts import render
from helloword.helloWeb.models import User
from django.http import HttpResponse


# Create your views here.
#跳转到登录界面
def login(request):
    return render(request,'index.html')
#跳转到登主界面
def main(request):
    return render(request,'tables.html')

#验证用户的用户名和密码是否正确
def verify(request):
    #判断是属于什么请求
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        result = {}
        try:
            #判断用户名和密码是否正确
            user = User.objects.get(user_name=username)
            if password == user.user_password:
                result = 1
            else:
                result = 0

        except:
            # 用户不存在
            result = -1
        result = json.dumps(result)
        #返回信息给页面
        return HttpResponse(result)
