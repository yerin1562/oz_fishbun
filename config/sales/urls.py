from django.urls import path

from .views import (ProductView, SalesRecordView, SalesItemView)

# config.url에서 ""로 지정했으므로 도메인 별로 url을 명시해줍니다.
urlpatterns = [
    path("stores/", ProductView.as_view(), name="products"),
    path("sales_record/", SalesRecordView.as_view(), name="sales_record"),
    path("sales_item/", SalesItemView.as_view(), name="sales_item"),
]
