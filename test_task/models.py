from django.db import models
from test_task.choices import STATUS_CHOICES


class Payment(models.Model):
    """" Payments """
    datetime = models.DateTimeField(auto_now_add=True)
    amount = models.BigIntegerField()
    purpose_of_payment = models.CharField(max_length=320)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
