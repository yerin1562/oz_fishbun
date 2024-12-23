from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # include를 사용하여 users/ 로 들어오는 모든요청을 users.urls로 연결하도록 설정합니다.
    path("users/", include("users.urls")),
    # stores 앰은 앱안에서 사용하는 모델이 많으므로 ""로 설정합니다.
    path("", include("stores.urls")),
]
