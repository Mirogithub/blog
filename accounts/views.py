from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .forms import *
from django.views.generic import View
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreate(View):
    template = 'accounts/registration_create_form.html'
    def get(self, request):
        form= UserAdminCreationForm()
        return render(request, self.template, context={'form':form})

    def post(self, request):
        bound_form = UserAdminCreationForm(request.POST or None)
        if bound_form.is_valid():
            new_obj = UserAdminCreationForm(request.POST).save()
            return redirect(reverse('articlelist_url'))
        return render(request, self.template, context={'form':bound_form})


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(request.POST)
        print("sssssssss")
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('articlelist_url')
        else:
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('registration_url')
