from django.urls import path

from .views import (AuthEmployeeView, EmployeeDetailView, EmployeeView,
                    StoreDetailView, StoreView)

# config.url에서 ""로 지정했으므로 도메인 별로 url을 명시해줍니다.
urlpatterns = [
    path("stores/", StoreView.as_view(), name="stores"),
    path("stores/<int:pk>/", StoreDetailView.as_view(), name="store"),
    path("employees/", EmployeeView.as_view(), name="employees"),
    path("employees/<int:pk>/", EmployeeDetailView.as_view(), name="employee"),
    path("employees/detail/", AuthEmployeeView.as_view(), name="employee"),
]
