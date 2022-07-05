from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from django.http import JsonResponse
from .serializers import AdminSerializer
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt

class AdminSignup(generics.GenericAPIView):
    serializer_class = AdminSerializer

    # @csrf_exempt
    def post(self, request, *args, **kwargs):
        try:
            request.data._mutable = True
            request.data["password"]=make_password(request.data["password"]) #It will Hash the password
            request.data._mutable = False
            print("here")
            admin = self.serializer_class(data=request.data)
            if admin.is_valid():
                admin.save()
                return JsonResponse({"status": "success", "message": admin.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
