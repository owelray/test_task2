from django.urls import path
from . import views

urlpatterns = [
    path('', views.PaymentListView.as_view()),
    path('edit/<int:payment_id>', views.EditPaymentView.as_view()),
    path('delete/<int:payment_id>', views.DeletePaymentView.as_view()),
]
