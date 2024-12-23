from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer, UserDetailSerializer


# APIView를 상속받는 UserView라는 클래스를 작성합니다.
class UserView(APIView):
    # post 형식으로 요청이 왔을 경우를 처리하는 메서드를 작성합니다.
    def post(self, request):
        # 요청으로 들어온 데이터를 역직렬화 하여 serializer라는 변수로 선언합니다
        serializer = UserSerializer(data=request.data)
        # ModelSerializer의 is_valid 매서드를 사용하여 데이터 유효성 검사를 합니다.
        if serializer.is_valid():
            # 유효한 데이터일 경우 save 메서드를 사용하여 데이터를 저장합니다.
            serializer.save()
            # 저장한 데이터와 함께 HTTP_201_CREATED 응답코드를 반환합니다.
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 오류가 있다면 errors 메서드를 사용하여 오류와 함께
        # HTTP_400_BAD_REQUEST 응답코드를 반환합니다.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # get 형식으로 요청이 왔을 경우를 처리하는 메서드를 작성합니다.
    def get(self, request):
        # User 모델의 매니저(objects)를 활용하여 객체를 조회합니다.
        user = User.objects.all()
        # all 메서드는 무조건 리스트를 반홤(내용이 없는 경우 빈리스트를 반환)하므로
        # user가 [] 빈리스트인지 확인합니다.
        if not user.exists():
            # user가 [] 빈리스트라면 {"error": "No users found"}라는 메세지와 함께
            # HTTP_404_NOT_FOUND 응답코드를 반환합니다.
            return Response(
                {"error": "No users found"}, status=status.HTTP_404_NOT_FOUND
            )
        # 데이터를 직렬화 하여 serializer 변수로 선언합니다.
        # 데이터(객체)가 둘 이상일 경우 many=True 옵션을 사용하여
        # 리스트 형태로 반환하도록 합니다.
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    # 매개변수로 pk를 포함하는 get 형식으로 요청이 왔을 경우를 처리하는 메서드를 작성합니다.
    def get(self, request, pk):
        # 매개변수로 들어온 pk를 사용하여 User를 조회합니다.
        user = User.objects.get(pk=pk)
        # 조회한 데이터를 직렬화 합니다.
        serializer = UserDetailSerializer(user)
        # 데이터와 합께 HTTP_200_OK 응답코드를 반환합니다.
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        
class AuthUserDetailView(APIView):
    # API 뷰에 인증된 사용자만 접근할 수 있도록 설정합니다.
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # 요청에 포함된 인증된 유저정보를 사용하여 user 변수로 선언합니다.
        user = request.user
        # 해당 유저 정보를 역직렬화 하여 serializer라는 변수로 선언합니다. 
        serializer = UserDetailSerializer(user)
        # 데이터와 함께 HTTP_200_OK 응답코드를 반환합니다.
        return Response(serializer.data, status=status.HTTP_200_OK)
