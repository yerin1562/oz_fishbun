# 남은 앱들의 serializer와 views urls 작성하기
# 단 get, post 메서드만 만들면 됩니다!!

# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import RawMaterial, Supplier, OrderRecord, Stock
from .serializers import (RawMaterialSerializer, SupplierSerializer,
                            OrderRecordSerializer, StockSerializer)


class RawMaterialView(APIView):
    def get(self, request):
        raw_materials = RawMaterial.objects.all()
        serializer = RawMaterialSerializer(raw_materials, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        raw_material = RawMaterialSerializer(data=request.data)
        if raw_material.is_valid():
            raw_material.save()
            return Response(raw_material.data, status=status.HTTP_201_CREATED)
        return Response(raw_material.errors, status=status.HTTP_400_BAD_REQUEST)


class SupplierView(APIView):
    def get(self, request, pk):
        suppliers = Supplier.objects.get(pk=pk)
        serializer = SupplierSerializer(suppliers)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        supplier = SupplierSerializer(data=request.data)
        if supplier.is_valid():
            supplier.save()
            return Response(supplier.data, status=status.HTTP_201_CREATED)
        return Response(supplier.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderRecordView(APIView):
    def get(self, request, pk):
        order_records = OrderRecord.objects.get(pk=pk)
        serializer = OrderRecordSerializer(order_records)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        order_record = OrderRecordSerializer(data=request.data)
        if order_record.is_valid():
            order_record.save()
            return Response(order_record.data, status=status.HTTP_201_CREATED)
        return Response(order_record.errors, status=status.HTTP_400_BAD_REQUEST)

class StockView(APIView):
    def get(self, request, pk):
        stocks = Stock.objects.get(pk=pk)
        serializer = StockSerializer(stocks)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        stock = StockSerializer(data=request.data)
        if stock.is_valid():
            stock.save()
            return Response(stock.data, status=status.HTTP_201_CREATED)
        return Response(stock.errors, status=status.HTTP_400_BAD_REQUEST)
