from django.shortcuts import render, redirect
from django.views.generic import *
from django.views.generic import ListView, TemplateView
from django.forms import inlineformset_factory
from owner.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from cars.models import *
from customer.models import *
from customer.forms import *
from django.http import JsonResponse, HttpResponse
from cars.forms import CreateCarForm
from user.models import FeedbackModel
from user.forms import FeedbackForm

# Create your views here.
class CustomerProfile(LoginRequiredMixin, TemplateView):
    template_name = 'customer/customer_profile.html'

class CustomerUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomerUpdateForm
    template_name = 'customer/carupdate.html'
    success_url = '/customerprofile/'

class CustomerDashboard(TemplateView):
    template_name = 'customer/customer_dashboard.html'
    extra_context = {
        'carlist':Car.objects.all(),
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carlist'] = context['carlist'].filter(availability=True)
        return context

class BookView(LoginRequiredMixin, View):
    def post(self, request):
        cars = request.POST.get('cars')
        form = ReservationModel(
            r_user=self.request.user,
            r_car=Car.objects.filter(id=cars)[0],
            price=Car.objects.filter(id=cars).values_list('rentalrate')[0][0]
        )
        form.placeOrder()
        av = Car.objects.get(id=cars)
        av.availability = False
        av.save()
        return redirect('payment')

class PaymentView(LoginRequiredMixin, View):
    def get(self,request):
        form = PaymentForm
        ptype = PaymentTypeModel.objects.all()
        contaxt ={'form':form,
                  'ptype':ptype,}
        return render(request, 'customer/paymentdone.html',contaxt)
    def post(self,request):
        order = ReservationModel.objects.all().last()
        price = ReservationModel.objects.filter(id=order.id).values_list('price')[0][0]
        form = PaymentModel(
            puser=self.request.user,
            pbook=order,
            ptype=request.POST['type'],
            pdone=True,
            price=price
        )
        form.paymentSave()
        return redirect('customerdashboard')

class CustomerBookedCarListView(LoginRequiredMixin, TemplateView):
    template_name = 'customer/bookedcar.html'
    extra_context = {
        'resev':ReservationModel.objects.all()
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resev'] = context['resev'].filter(r_user=self.request.user)
        return context

class FeedbackView(LoginRequiredMixin, CreateView):
    model = FeedbackModel
    form_class = FeedbackForm
    template_name = "Customer/feedback.html"
    success_url = "/"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)