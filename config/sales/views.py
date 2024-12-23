# 남은 앱들의 serializer와 views urls 작성하기
# 단 get, post 메서드만 만들면 됩니다!!

# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, SalesRecord, SalesItem
from .serializers import (ProductSerializer, SalesItemSerializer,
                            SalesRecordSerializer)


class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        product = ProductSerializer(data=request.data)
        if product.is_valid():
            product.save()
            return Response(product.data, status=status.HTTP_201_CREATED)
        return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)


class SalesItemView(APIView):
    def get(self, request, pk):
        salesitems = SalesItem.objects.get(pk=pk)
        serializer = SalesItemSerializer(salesitems)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        salesitem = SalesItemSerializer(data=request.data)
        if salesitem.is_valid():
            salesitem.save()
            return Response(salesitem.data, status=status.HTTP_201_CREATED)
        return Response(salesitem.errors, status=status.HTTP_400_BAD_REQUEST)

class SalesRecordView(APIView):
    def get(self, request, pk):
        sales_records = SalesRecord.objects.get(pk=pk)
        serializer = SalesRecordSerializer(sales_records)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        sales_record = SalesRecordSerializer(data=request.data)
        if sales_record.is_valid():
            sales_record.save()
            return Response(sales_record.data, status=status.HTTP_201_CREATED)
        return Response(sales_record.errors, status=status.HTTP_400_BAD_REQUEST)
