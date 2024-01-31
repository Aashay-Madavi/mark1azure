from rest_framework.serializers import ModelSerializer
from orderTrack.models import OrderTrack


class TrackingSerializer(ModelSerializer):
    class Meta:
        model = OrderTrack
        fields = '__all__'
