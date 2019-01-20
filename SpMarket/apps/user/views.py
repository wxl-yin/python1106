from django.shortcuts import render

# Create your views here.
from django.views import View


class LoginView(View):
    """登录视图"""
    def get(self,request):
        return render(request,'user/login.html')


    def post(self,request):
        pass