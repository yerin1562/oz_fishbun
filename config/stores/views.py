from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Employee, Store
from .serializers import (AuthEmployeeSerializer, EmployeeSerializer,
                            StoreSerializer)


# Create your views here.
class StoreView(APIView):
    def get(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        store = StoreSerializer(data=request.data)
        if store.is_valid():
            store.save()
            return Response(store.data, status=status.HTTP_201_CREATED)
        return Response(store.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreDetailView(APIView):
    def get(self, request, pk):
        store = Store.objects.get(pk=pk)
        serializer = StoreSerializer(store)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EmployeeView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        employee = EmployeeSerializer(data=request.data)
        if employee.is_valid():
            employee.save()
            return Response(employee.data, status=status.HTTP_201_CREATED)
        return Response(employee.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthEmployeeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        employee = Employee.objects.get(user=user)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user

        if Employee.objects.filter(user=user):
            authuser = True
        else:
            authuser = False

        if authuser == False:
            serilalzer = AuthEmployeeSerializer(data=request.data)

            if serilalzer.is_valid():
                serilalzer.save(user=user)
                return Response(serilalzer.data, status=status.HTTP_201_CREATED)
            return Response(serilalzer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"message": "너 이미 직장 있잖아!"}, status=status.HTTP_400_BAD_REQUEST
            )


class EmployeeDetailView(APIView):
    def get(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        serializer = StoreSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)