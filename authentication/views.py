from django.shortcuts import redirect, render
from django.views import View

from django.contrib.auth import logout


class Home(View):
    def get(self, request):
        if request.user.is_authenticated():
            return redirect('dashboard')
        else:
            return redirect('auth:login')


class Login(View):
    login_template = 'login.html'

    def get(self, request):
        return render(request, self.login_template)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('auth:login')