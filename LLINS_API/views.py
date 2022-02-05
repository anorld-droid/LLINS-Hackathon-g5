from django.shortcuts import render
from django.http import JsonResponse

# third parties imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from LLINS_API.serializers import UserSerializer
from rest_framework import permissions


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "name": "Patrice",
            "age": 21,
            "course": "Computer Science"
        }
        return Response(data)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# def test_view(request):
#     data = {
#         "name": "Patrice",
#         "age": 21,
#         "course": "Computer Science"
#     }
#     return JsonResponse(data)
