from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login,logout
from django.views import View

from .forms import CustomLoginForm,RegisterForm

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "accounts/register.html", context={"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():  # Corrected this line
            form.save()
            return redirect('accounts:login')  # Corrected this line
        else:
            return render(request, "accounts/register.html", context={'form': form})  # Corrected this line

class LoginView(View):
    def get(self, request):
        form = CustomLoginForm()
        return render(request, 'accounts/login.html', context={"form": form})

    def post(self, request):
        form = CustomLoginForm(request,request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']  # Corrected line
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('home')
 
        return render(request, 'accounts/login.html', context={"form": form})

def logout_view(request):
    logout(request)
    return redirect("home")