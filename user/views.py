from django.shortcuts import render, redirect
from user.forms import *
from django.views.generic.edit import FormView, CreateView
from django.views.generic import ListView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

class UserLoginView(LoginView):
    template_name = 'user/sign-in.html'
    redirect_authenticated_user = True

    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_owner:
                return '/owner/ownerdashboard/'
            else:
                return '/'

class OwnerRegisterView(FormView):
    model = User
    form_class = OwnerRegisterForm
    template_name = 'user/sign-up.html'
    success_url = '/user/login/'
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            subject = "Welcome to CarRental site"
            message = f"Welcome dear, {user.first_name} {user.last_name},\nYour registrations as an Owner is successful.\nThank You"
            email_form = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            try:
                res = send_mail(subject, message, email_form, recipient_list)
                if res > 0:
                    print('mail sent')
                else:
                    print('mail not sent')
            except Exception as e:
                print(e)
            login(self.request, user)
        return super(OwnerRegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('ownerdashboard')
        return super(OwnerRegisterView, self).get(*args, **kwargs)


class CustomerRegisterView(FormView):
    model = User
    form_class = CustomerRegistrationForm
    template_name = 'user/sign-up.html'
    success_url = '/user/login/'
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            subject = "Welcome to CarRental site"
            message = f"Welcome dear, {user.first_name} {user.last_name},\nYour registrations as an Customer is successful.\nThank You"
            email_form = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            try:
                res = send_mail(subject, message, email_form, recipient_list)
                if res > 0:
                    print('mail sent')
                else:
                    print('mail not sent')
            except Exception as e:
                print(e)
            login(self.request, user)
        return super(CustomerRegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('customerdashboard')
        return super(CustomerRegisterView, self).get(*args, **kwargs)

class ChoiseForSignUp(TemplateView):
    template_name = "user/choicesignup.html"

