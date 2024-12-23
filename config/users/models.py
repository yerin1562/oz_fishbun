# AbstractBaseUser: User 모델을 커스터마이징할 때 사용하는 추상클래스
# BaseUserManager: User 모델에서 사용하는 매니저 클래스를 정의할 때 사용하는 추상클래스
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from common.models import BaseModel


# BaseUserManager를 상속받는 UserManager라는 매니저 클래스를 작성합니다.
class UserManager(BaseUserManager):
    # 비즈니스 로직들을 작성합니다.
    
    # active_user: 활성화 된(is_active=True) 유저만 조회라는 로직
    def active_user(self):
        return self.filter(is_active=True)

    # active_staff: 활성화 된 유저중 직원(is_staff=True)만 조회하는 로직
    def active_staff(self):
        return self.filter(is_staff=True, is_active=True)

    # withdraw_user: 회원 탈퇴한 일반 유저를 조회하는 로직
    def withdraw_user(self):
        return self.filter(is_active=False, is_staff=False)

    # withdraw_staff: 회원 탈퇴한 직원을 조회하는 로직
    def withdraw_staff(self):
        return self.filter(is_staff=True, is_active=False)
        
    # _create_user: 유저 생성시에 사용되는 헬퍼 메서드
    def _create_user(self, email, password, **extra_fields):
        # normalize_email: 이메일을 정규화 해줍니다.
        email = self.normalize_email(email)
        # 정규화한 이메일과 추가 데이터(**extra_fields)를 모델로 정의합니다.
        user = self.model(email=email, **extra_fields)
        # set_password: 비밀번호를 해시화 해줍니다.
        user.set_password(password)
        # svae: db에 user를 저장 해줍니다.
        user.save(using=self._db)
        return user
        
    # create_user: 일반 유저 생성시에 사용하는 메서드
    def create_user(self, email, password=None, **extra_fields):
        # extra_fields에 is_staff가 존재하지 않을때 False로 추가/지정합니다.
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        # 생성 된 내용을 _create_user라는 헬퍼메서드로 전달합니다.
        return self._create_user(email, password, **extra_fields)
    
    # create_superuser: 관리자 유저 생성시에 사용하는 메서드
    def create_superuser(self, email, password, **extra_fields):
        # extra_fields에 is_staff가 존재하지 않을때 True로 추가/지정합니다.
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # 생성 된 내용을 _create_user라는 헬퍼메서드로 전달합니다.
        return self._create_user(email, password, **extra_fields)
        

# AbstractBaseUser를 상속받는 User라는 모델을 작성합니다.        
class User(AbstractBaseUser, BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.TextField(null=True)
    contact = models.CharField(max_length=50, null=True)
    # choices 옵션으로 ENU자료형과 비슷한 역할을 할 수 있도록 합니다.
    gender = models.CharField(
        max_length=6, choices=[("MALE", "Male"), ("FEMALE", "Female")]
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # AbstractBaseUser의 기본 필드인 last_login을 사용하지 않는다고 명시적으로 작성합니다.
    last_login = None

    # USERNAME_FIELD를 설정하여 auth_user의 인증방식을 사용할 때
    # 기본으로 지정되어있는 username 필드를 email 필드로 대체 한다고 명시적으로 작성합니다.
    USERNAME_FIELD = "email"

    # UserManager라는 매니저를 선언하고 User모델과 연결합니다.
    objects = UserManager()

    # 메타데이터를 정의하는 내부 클래스인 Meta라는 클래스를 작성합니다.
    class Meta:
        # 실제 데이터베이스에 저장될 테이블 이름을 설정합니다.
        db_table = "users"
        # 관리자 페이지 등 에서 모델의 이름을 단수형으로 설정합니다.
        verbose_name = "User"
        # verbose_name의 복수형을 설정합니다.
        verbose_name_plural = "Users"
        # 조회시에 기본 정렬 순서를 설정합니다.
        ordering = ["last_name", "first_name"]
        
        # 이외에도 많은 옵션들이 있습니다. 공식문서를 참고하세요!


    # __str__: 객체를 사람이 읽기 쉬운 문자열로 표현할 때 사용합니다.
    def __str__(self):
        # 객체를 출력할 때의 형태를 지정합니다.
        return f"{self.first_name} {self.last_name} ({self.email})"
        
    # has_perm: 사용자가 특정 권한을 갖고있는지 True / False로 반환합니다.
    def has_perm(self, perm, obj=None):
        if self.is_superuser:
            return True
        return False
    
    # has_module_perms: 사용자가 특정 애플리케이션에
    # 접근 할 수 있는지 Treu / False로 반환합니다.
    def has_module_perms(self, app_label):
        if self.is_superuser:
            return True
        return False

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
