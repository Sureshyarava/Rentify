from rest_framework.serializers import ModelSerializer
from .models import CustomUser

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

    def create(self, validated_data):
        user = CustomUser(
            username = validated_data['username'],
            password = validated_data['password'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            phone_number = validated_data['phone_number']
        )
        user.save()
        return user


class BasicUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','phone_number','email']