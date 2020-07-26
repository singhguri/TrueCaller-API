from rest_framework.serializers import ModelSerializer
from .models import User, Spam


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserSearchSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["user_id", "name", "phnNumber", "email", "isSpam", "isRegistered"]


class RegisteredUserSrializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["user_id", "phnNumber", "name", "isSpam", "isRegistered"]


class SpamSerializer(ModelSerializer):
    class Meta:
        model = Spam
        fields = "__all__"

