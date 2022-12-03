from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login


class LoginAPIView(APIView):
    def post(self, request:Request):
        username = request.data['username']
        password = request.data['password']

        if username and password:
            user = authenticate(request=request, username=username, password=password)
            if user is None:
                raise PermissionDenied
        else:
            raise PermissionDenied
        login(request, user=user)
        return Response(status=status.HTTP_200_OK)

