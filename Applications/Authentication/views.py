from cmath import log
from django.contrib import messages
from django.shortcuts import render
from django.views import View
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth import authenticate, login, logout

class RegisterView(View):
    """
    Class based view for rendering the registration form as well as registering new users.
    """
    def get(self, request):
        form = NewUserForm()
        context = {
            'form' : form
        }
        return render(request, 'Authentication/register.html', context)

    def post(self, request):
        form = NewUserForm(request, data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Login with your credentials.')
            return redirect('/auth/login/')
        else:
            messages.error(request, 'Registration error.')
            return redirect(self.request.path_info)   

class LoginView(View):
    """
    Class based view to login a user.
    """
    def get(self, request):
        form = AuthenticationForm()
        context = {
            'form' : form
        }
        return render(request, 'Authentication/login.html', context)

    def post(self, request):
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect(self.request.path_info)
        else:
            messages.error(request, 'Invalid input.')
            return redirect(self.request.path_info)   

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out successfully.')
        return redirect('/auth/login/')  

class PasswordResetView(View):
    def get(self, request):
        form = PasswordResetForm()
        context = {
            'form' : form
        }
        return render(request, 'Authentication/passwordreset.html', context)

    def post(self, request):
        form = PasswordResetForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('/auth/login/')                               