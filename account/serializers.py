import email
from tkinter.ttk import Style
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from account.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    # we are writing this bcuz we need confirm password field in 
    # our registration request

    password2 = serializers.CharField(
        # Style={'input_type':'password'},
        # write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'name','tc','password', 'password2']
        extra_kwargs={
            'password':{'write_only':True},
        }

    # Validating password and confirm password while registration
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Passwords don't match.")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email','password']