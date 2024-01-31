from django.db import models
from orders.models import Orders
# Create your models here.


class OrderTrack(models.Model):
    confirmed = models.BooleanField(default=False)
    dispatched = models.BooleanField(default=False)
    shipped = models.BooleanField(default=False)
    in_transit = models.BooleanField(default=False)
    out_for_delivery = models.BooleanField(default=False)
    final_status = models.CharField(default="pending", max_length=100)
    orderId = models.ForeignKey(Orders, on_delete=models.CASCADE)

    def __str__(self):
        return 'Tracking Id : ' + str(self.id)
