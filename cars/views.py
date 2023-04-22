from django.shortcuts import render
from django.views.generic import *
from cars.models import *
from cars.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
class CreateCarView(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CreateCarForm
    success_url = '/owner/ownerdashboard/'
    # def post(self, request, *args, **kwargs):
    #     return JsonResponse(request.POST)
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateCarView, self).form_valid(form)

class DeleteCarView(LoginRequiredMixin, DeleteView):
    model = Car
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    success_url = '/owner/ownerdashboard/'

class UpdateCarView(LoginRequiredMixin, UpdateView):
    model = Car
    template_name = 'owner/carupdate.html'
    form_class = CreateCarForm
    success_url = '/owner/ownerdashboard/'


class DetailCarView(LoginRequiredMixin, DetailView):
    model = Car
    template_name = 'customer/cardetails.html'
    context_object_name = "car"


