from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import AuthUserDetailView, UserDetailView, UserView

# url 경로와 뷰를 매핑해주는 리스트를 작성합니다.
urlpatterns = [
    # path("경로", 사용할 뷰 클래스, url 패턴 이름)
    path('', UserView.as_view()),
    # <자료형(데이터 형식):매개변수>의 형태로 매개변수를 동적으로 처리하는 하도록 설정합니다.
    path('<int:pk>/', UserDetailView.as_view(), name='user'),
    path('detail/', AuthUserDetailView.as_view(), name='user_detail'),
    path('login/', TokenObtainPairView.as_view(), name='user_login'),
    path('refresh/', TokenRefreshView.as_view(), name='user_refresh'),
]