from django.shortcuts import render,redirect
from django.views.generic import *
from owner.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from cars.models import Car
from cars.forms import CreateCarForm
from customer.models import ReservationModel,PaymentModel
from owner.forms import UpdateBookingStatusForm
from user.models import FeedbackModel
from user.forms import FeedbackForm
from django.http import JsonResponse, HttpResponse
# Create your views here.
class OwnerProfile(LoginRequiredMixin, TemplateView):
    template_name = 'owner/owner_profile.html'
    extra_context = {
        'form': CreateCarForm,
    }

class OwnerUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = OwnerUpdateForm
    template_name = 'owner/update.html'
    success_url = '/owner/ownerprofile/'

class OwnerDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'owner/owner_dashboard.html'
    extra_context = {
        'carlist': Car.objects.all(),
        'form': CreateCarForm,
        }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carlist'] = context['carlist'].filter(user=self.request.user)
        return context
class BookedListView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        reves = ReservationModel.objects.all()
        ls =[]
        for i in reves:
            if i.r_car.user == self.request.user:
                ls.append(i)
        context = {
            'resev': ls,
            'form2': UpdateBookingStatusForm,
            'form': CreateCarForm,
        }
        return render(request, 'owner/castomer_booked_list.html', context)

class OwnerFeedbackView(LoginRequiredMixin, TemplateView):
    template_name = 'owner/feedback.html'

class BookingStatusUpdate(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        id = request.POST['uid']
        form = ReservationModel.objects.get(id=id)
        form.status = request.POST['status']
        if request.POST['status'] == "RETURN":
            av = Car.objects.get(id=form.r_car.id)
            av.availability = True
            av.save()
        elif request.POST['status'] == "CANCEL":
            av = Car.objects.get(id=form.r_car.id)
            av.availability = True
            av.save()
        form.save()
        return redirect('bookedlist')

class FeedbackView(LoginRequiredMixin, TemplateView):
    template_name = "owner/feedback.html"
    extra_context = {
        'form': CreateCarForm,
        'form2': FeedbackForm,
    }

    def post(self, request):
        form = FeedbackModel(user=self.request.user,
                             email=request.POST['email'],
                             feedback=request.POST['feedback'])
        form.save()
        return redirect('/owner/ownerdashboard/')