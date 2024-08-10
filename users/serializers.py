# from rest_framework import serializers
#
# from users.models import User, Payment
#
#
# class PaymentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Payment
#         fields = '__all__'
#
#
# class UserSerializer(serializers.ModelSerializer):
#     payments = PaymentSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = User
#         fields = ['id', 'email', 'phone', 'city', 'avatar', 'payments']
from rest_framework.serializers import ModelSerializer

from users.models import User, Donat


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class DonatSerializer(ModelSerializer):
    class Meta:
        model = Donat
        fields = '__all__'
