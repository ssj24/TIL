from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from .serializers import TodoSerializer, UserCreationSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes, authentication_classes
# from rest_framework.authentication import JSONWebTokenAuthentication
from .models import Todo
from django.http import HttpResponseForbidden

User = get_user_model()

# Create your views here.
@api_view(['POST']) # 무조건 배열로
# settings.py에서 REST_FRAMEWORK를 설정해줘서 아래 두 데코레이터는 안 써도 된다.
# # 인증 받은 사용자만 허가(로그인 여부 체크)
# @permission_classes((IsAuthenticated,)) # 튜플로..
# # jwt 인증
# @authentication_classes((JSONWebTokenAuthentication,))
def todo_create(request):
    serializer = TodoSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=400)

@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, id): #api를 짤 때는 쟝고에서만 쓰는 게 아니니까 pk보다는 id
    todo = get_object_or_404(Todo, pk=id)
    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data) #기존: todo, 새로 작성할 거: data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    else: #elif request.method == 'DELETE'
        todo.delete()
        # 204: 해당하는 컨텐츠가 없는 경우(삭제를 했기 때문에 해당 데이터가 이제 존재하지 않음을 알려줌)
        return Response(status=204)

@api_view(['POST'])
@permission_classes((AllowAny,)) # 회원가입은 인증 없어도 할 수 있어야 하니까
def user_signup(request):
    serializer = UserCreationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        # print(serializer.data) #프린트했을 때 비밀번호가 그대로 보이면 안 됨
        return Response({'message': '회원가입이 성공적으로 완료되었습니다.'})

@api_view(['GET'])
def user_detail(request, id):
    user = get_object_or_404(User, pk=id)
    if request.user != user:
        return HttpResponseForbidden()
        # return Response(status=403) # 위와 똑같은 데 위에 거는 쟝고 built-in
    serializer = UserSerializer(user)
    return Response(serializer.data)