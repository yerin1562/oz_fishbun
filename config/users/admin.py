from django.contrib import admin
from .models import User


# User 모델을 Django Admin에 등록하는 데코레이터
@admin.register(User)
# Admin 페이지에서 보여지는 방식이나 동작을 정의하는 UserAdmin를 작성합니다.
class UserAdmin(admin.ModelAdmin):
    # pass를 사용하여 클래스의 내용을 비워두면 기본 관리자 페이지설정으로 설정됩니다.
    pass
