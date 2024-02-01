from django.db import models
from orders.models import Orders
# Create your models here.


class OrderTrack(models.Model):

    confirmed = models.JSONField(
        blank=True, default=dict)
    dispatched = models.JSONField(
        blank=True, default=dict)
    shipped = models.JSONField(
        blank=True, default=dict)
    in_transit = models.JSONField(
        blank=True, default=dict)
    out_for_delivery = models.JSONField(
        blank=True, default=dict)
    final_status = models.CharField(default="pending", max_length=100)
    orderId = models.ForeignKey(Orders, on_delete=models.CASCADE)

    def __str__(self):
        return 'Tracking Id : ' + str(self.id)+' ' + str(self.date)
