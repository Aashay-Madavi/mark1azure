from rest_framework.serializers import ModelSerializer
from orderTrack.models import OrderTrack
from rest_framework.serializers import ValidationError


class TrackingSerializer(ModelSerializer):
    class Meta:
        model = OrderTrack
        fields = '__all__'

    def validate_put(self, data):

        confirmed = self.instance.confirmed
        dispatched = self.instance.dispatched
        shipped = self.instance.shipped
        in_transit = self.instance.in_transit
        out_for_delivery = self.instance.out_for_delivery
        final_status = self.instance.final_status

        keys = data.keys()
        stat = data.get('final_status')
        print(stat)
        for k in keys:

            if confirmed and dispatched and k == 'confirmed':

                raise ValidationError({'error': "Confirmed can't be Updated"})
            if dispatched and shipped and k == 'dispatched':
                raise ValidationError("Dispatched can't be Updated")
            if shipped and in_transit and k == 'shipped':
                raise ValidationError({'error': "Shipped can't be Updated"})
            if in_transit and out_for_delivery and k == 'in_transit':
                raise ValidationError({'error': "in_transit can't be Updated"})
            if out_for_delivery and final_status and k == 'out_for_delivery':
                raise ValidationError(
                    {'out_for_deliveryerror': " can't be Updated"})

            if final_status == stat:

                raise ValidationError(
                    {'error': "Updating same status"})

            if stat and stat != 'delivered':
                raise ValidationError({'error': 'entering wrong status'})
            if stat == 'delivered':
                if confirmed and dispatched and shipped and in_transit and out_for_delivery:
                    self.instance.final_status = stat
                else:
                    raise ValidationError(
                        {'error': 'your order is delivered '})
            return data

    def validate(self, data):

        if self.instance is None:
            return data
        else:
            return self.validate_put(data)
