from rest_framework.serializers import ModelSerializer
from orderTrack.models import OrderTrack
from rest_framework.serializers import ValidationError


class TrackingSerializer(ModelSerializer):
    class Meta:
        model = OrderTrack
        fields = '__all__'

    def validate_put(self, data):
        status_mapping = {
            'confirmed': self.instance.confirmed,
            'dispatched': self.instance.dispatched,
            'shipped': self.instance.shipped,
            'in_transit': self.instance.in_transit,
            'out_for_delivery': self.instance.out_for_delivery,
            'final_status': self.instance.final_status,
        }
        final_status = data.get("final_status")
        keys = data.keys()
        request_status = None

        for key in keys:
            request_status = key

        try:
            current_status_index = list(
                status_mapping.keys()).index(request_status)

        except ValueError:
            raise ValidationError({'error': 'Invalid status provided.'})
        previous_status = list(status_mapping.keys())[current_status_index-1]
        if final_status and final_status != 'delivered':
            raise ValidationError({'error': 'You are entering wrong status'})
        elif final_status and self.instance.final_status == 'delivered':
            raise ValidationError(
                {'error': 'not allowed to change final status'})

        if current_status_index == 0 or status_mapping[list(status_mapping.keys())[current_status_index - 1]]:
            return data

        else:
            raise ValidationError(
                {'error': f'Cannot update to the {request_status} because order is not yet {previous_status}.'})

    def validate_post(self, data):
        status_meta = list(data.keys())
        final_status = data.get('final_status')
        given_attrs = list(data.get('confirmed').keys())
        requride_attrs = ['state', 'city', 'pincode', 'date']
        if final_status:
            raise ValidationError({'Tip': 'no need to mention final status'})

        if status_meta[0] == 'confirmed' and status_meta[1] == 'orderId':
            if given_attrs == requride_attrs:
                return data

            else:
                raise ValidationError(
                    {'error': 'Enter all fields properly'})
        else:
            raise ValidationError(
                {'error': 'order must be confirmed first'})

    def validate(self, data):
        if self.instance:
            return self.validate_put(data)
        else:
            return self.validate_post(data)
