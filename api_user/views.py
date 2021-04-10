from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api_user.models import User
from api_user.serializers import UserSerializer

from django.http import Http404
from rest_framework.views import APIView

from rest_framework import generics


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # 권한 부여 메소드
    def perform_create(self, serializer):
        serializer.save(name=request.user)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
# class UserList(APIView):
#     """
#     List all users, or create a new user
#     """
    
#     def get(self, request, format=None):
#         users = User.objects.all()
#         for user in users:
#             print(user.user_id)
#         users_serializer = UserSerializer(users, many=True)
#         return Response(users_serializer.data)
    
    
#     def post(self, request, pk, format=None):
#         user_serializer = UserSerializer(data=request.data)
#         if user_serializer.is_valid():
#             user_serializer.save()
#             print('POST: user시리얼: ', user_serializer.data)
#             return Response(user_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 

class UserDetail(APIView):
    
    def get_object(self, pk):    
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    
    
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)
    

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        user_serializer = UserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

