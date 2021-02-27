from rest_framework import serializers
from cars.models import Car


class CarDetailSerializer(serializers.ModelSerializer):
    # non default (can't change user)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = '__all__'  # all fields


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'vin', 'user')

