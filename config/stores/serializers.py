from rest_framework import serializers

from .models import Employee, Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class AuthEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("code", "type", "store")