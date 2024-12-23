# 직렬화(Serialization): 객체를 JSON형식으로 변환합니다.
# 역직렬화(Deserialization): JSON형식을 객체로 변환합니다.
from rest_framework import serializers
from .models import User

# ModelSerializer를 상속받는 UserSerializer 클래스를 작성합니다.
class UserSerializer(serializers.ModelSerializer):
    # password를 쓰기 전용으로 설정하여 응답시에 반환하지 않도록 설정합니다.
    password = serializers.CharField(write_only=True)

    class Meta:
        # 직렬화할 모들을 설정합니다.
        model = User
        # 직렬화할 필드를 설정합니다.
        fields = "__all__"

    # User객체를 생성할 때 사용할 create메서드를 작성합니다.
    def create(self, validated_data):
        # @gmail.com로 끝나는 이메일만 허용하도록 이메일의 유효성 검사를 추가합니다.
        if not validated_data.get("email").endswith("@gmail.com"):
            raise serializers.ValidationError("너 지메일 아니잖아!")
        user = User(**validated_data)
        user.set_password(validated_data.get("password"))
        user.save()
        return user


# User의 세부 정보만 직렬화하는 UserDetailSerializer 클래스를 작성합니다.
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "address", "contact", "gender", )