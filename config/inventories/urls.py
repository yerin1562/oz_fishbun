from django.urls import path

from .views import (SupplierView, OrderRecordView, RawMaterialView,
                    StockView)

# config.url에서 ""로 지정했으므로 도메인 별로 url을 명시해줍니다.
urlpatterns = [
    path("suppliers/", SupplierView.as_view(), name="suppliers"),
    path("orders/records", OrderRecordView.as_view(), name="order_record"),
    path("RawMaterial/", RawMaterialView.as_view(), name="raw_material"),
    path("stock/", StockView.as_view(), name="stock"),
]
