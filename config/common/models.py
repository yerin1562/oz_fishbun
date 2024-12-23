from django.db import models


# 장고의 기본 모델인 models.Model을 사용하여 BaseModel이라는 모델 클래스를 작성합니다.
class BaseModel(models.Model):
    # 데이터 생성시간(created_at), 수정시간(updated_at)을 기록하는 필드(컬럼)을 만들고
    # DateTimeField의 auto_now_add=True, auto_now=True 옵션으로
    # 생성시간과 수정시간을 기록합니다.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 메타데이터를 정의하는 내부 클래스인 Meta라는 클래스를 작성합니다.
    class Meta:
        # 추상클래스로 설정해주어서 데이터베이스 테이블로 생성되지 않게 지정합니다.
        abstract = True