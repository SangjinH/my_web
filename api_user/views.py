from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from .models import User

# token
class UserView(APIView):
    """
    POST /user
    """
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    

    ''' 
    Get /user
    Get /user/{user_id}
    '''
    def get(self, request, **kwargs):
        if kwargs.get('user_id') is None:
            user_queryset = User.objects.all()
            user_queryser_serializer = UserSerializer(user_queryset, many=True)
            return Response(user_queryser_serializer.data, status=status.HTTP_200_OK)
        else:
            user_id = kwargs.get('user_id')
            user_serializer = UserSerializer(User.objects.get(pk=user_id))
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        
    
    ''' 
    PUT /user/{user_id}
    '''
    def put(self, request, **kwargs):
        if kwargs.get('user_id') is None:
            return Response("invalid Request", status=status.HTTP_400_BAD_REQUEST)
        else:
            user_id = kwargs.get('user_id')
            user_object = User.objects.get(pk=user_id)

            update_user_serializer = UserSerializer(user_object, data=request.data)
            if update_user_serializer.is_valid():
                update_user_serializer.save()
                return Response(update_user_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)
        
    
    

    ''' 
    DELETE /user/{user_id}
    '''
    def delete(self, request, **kwargs):
        if kwargs.get('user_id') is None:
            return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)
        else:
            user_id = kwargs.get('user_id')
            user_object = User.objects.get(pk=user_id)
            user_object.delete()
            return Response("test ok", status=200)
