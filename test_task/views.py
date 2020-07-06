from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic.base import View
from .models import Payment
from .forms import PaymentCreateForm, PaymentEditForm


class PaymentListView(View):
    """ Shows a list of Payments and
        allows to perform CRUD operations on them """
    def get(self, request):
        list_of_payments = Payment.objects.all().order_by('id')
        form = PaymentCreateForm
        return render(request, 'index.html', {'form': form, 'payments': list_of_payments})

    def post(self, request):
        form = PaymentCreateForm(request.POST)
        if form.is_valid():
            payment = Payment()
            payment.amount = request.POST.get('amount')
            payment.purpose_of_payment = request.POST.get('purpose_of_payment')
            payment.save()
        return HttpResponseRedirect('/')


class EditPaymentView(View):
    """ Allows to edit existing Payment """
    def get(self, request, payment_id):
        payment = Payment.objects.get(id=payment_id)
        form_data = {'amount': payment.amount, 'purpose_of_payment': payment.purpose_of_payment,
                     'status': payment.status}
        form = PaymentEditForm(form_data)
        return render(request, 'edit.html', {'form': form, 'payment': payment})

    def post(self, request, payment_id):
        form = PaymentEditForm(request.POST)
        try:
            payment = Payment.objects.get(id=payment_id)
            if form.is_valid():
                payment.amount = request.POST.get('amount')
                payment.purpose_of_payment = request.POST.get('purpose_of_payment')
                payment.status = request.POST.get('status')
                payment.save()
            return HttpResponseRedirect('/')
        except Payment.DoesNotExist:
            return HttpResponseNotFound('<h2>Review not found</h2>')


class DeletePaymentView(View):
    """ Allows to delete existing payment """
    def get(self, request, payment_id):
        try:
            payment = Payment.objects.get(id=payment_id)
            payment.delete()
            return HttpResponseRedirect('/')
        except Payment.DoesNotExist:
            return HttpResponseNotFound('<h2>Payment not found</h2>')
