from rest_framework import serializers

from vehicle.models import Car, Moto


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CarDetailSerializer(serializers.ModelSerializer):
    car_with_moto = serializers.SerializerMethodField()

    def get_car_with_moto(self, obj):
        return Car.objects.filter(id=obj.id).first()

    class Meta:
        model = Car
        fields = ("name", "model", "year")


class MotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moto
        fields = "__all__"
