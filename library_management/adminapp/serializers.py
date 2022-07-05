from rest_framework import serializers
from .models import Admin
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class AdminSerializer(serializers.ModelSerializer):

        class Meta:
            model = Admin
            fields = ('email','password',)