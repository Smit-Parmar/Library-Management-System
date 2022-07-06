from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from django.http import JsonResponse
from .serializers import AdminSerializer
from django.contrib.auth.hashers import make_password
from .models import Admin
from rest_framework.permissions import AllowAny


class AdminSignup(generics.GenericAPIView):
    serializer_class = AdminSerializer

    def post(self, request, *args, **kwargs):
        try:# To avaid dict _mutable error
            request.data._mutable = True
            request.data["password"]=make_password(request.data["password"]) #It will Hash the password
            request.data._mutable = False
            admin = self.serializer_class(data=request.data)
            if admin.is_valid():
                admin.save()
                return JsonResponse({"status": "success", "message": admin.data}, status=status.HTTP_201_CREATED)
        except:
            request.data["password"]=make_password(request.data["password"]) #It will Hash the password
            admin = self.serializer_class(data=request.data)
            if admin.is_valid():
                admin.save()
                return JsonResponse({"status": "success", "message": admin.data}, status=status.HTTP_201_CREATED)
