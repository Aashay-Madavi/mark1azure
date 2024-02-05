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

        keys = data.keys()
        
        for key in keys:
            request_status = key

        try:
            current_status_index = list(
                status_mapping.keys()).index(request_status)

        except ValueError:
            raise ValidationError({'error': 'Invalid status provided.'})

        if current_status_index == 0 or status_mapping[list(status_mapping.keys())[current_status_index - 1]]:
            return data

        else:
            raise ValidationError(
                {'error': f'Cannot update to the {request_status}.'})

    def validate_post(self, data):
        for d in data:
            if d != 'confirmed':
                raise ValidationError("order must be confirmed first")
        return data

    def validate(self, data):
        if self.instance:
            return self.validate_put(data)
        else:
            return self.validate_post(data)
