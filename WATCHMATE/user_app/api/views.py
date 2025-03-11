from rest_framework.response import  Response
from .seializer import RegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def register(request):
    serializer = RegistrationSerializer(data=request.data)

    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['success'] = True
        data['username'] = account.username
        data['email'] = account.email

        token = Token.objects.get(user=account).key
        data['token'] = token
        return Response(data, status=status.HTTP_201_CREATED)

    else:
        data['success'] = False
        data['message'] = serializer.errors
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout_view(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)