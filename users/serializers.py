from rest_framework import serializers
from .models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'name', 'email', 'password',
                  'contactNo', 'dob', 'address')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # user = Users.objects.create(
        #     email=validated_data['email'], name=validated_data.get('name', ''), contactNo=validated_data.get('contactNo', ''), dob=validated_data.get('dob', None),
        #     address=validated_data.get('address', ''))
        user = Users.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
