from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from itertools import chain
from django.db.models import Q
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
import hashlib

from .models import User, Spam
from .serializers import (
    UserSerializer,
    UserSearchSerializer,
    SpamSerializer,
    RegisteredUserSrializer,
)


# Create your views here.


class UserList(APIView):
    authentication_classes = [
        TokenAuthentication,
    ]

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data["password"] = hashlib.md5(
            request.data["password"].encode("utf8")
        ).hexdigest()
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    authentication_classes = [
        TokenAuthentication,
    ]

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        phnNum = request.data["phnNumber"]
        try:
            user = User.objects.get(phnNumber=phnNum)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        phnNum = request.data["phnNumber"]
        try:
            user = User.objects.get(phnNumber=phnNum)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        phnNum = request.data["phnNumber"]
        try:
            user = User.objects.get(phnNumber=phnNum)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserSearch(APIView):
    authentication_classes = [
        TokenAuthentication,
    ]

    permission_classes = [
        IsAuthenticated,
    ]

    def findByName(self, search_name):
        result = User.objects.filter(
            Q(name__startswith=search_name) | Q(name__icontains=search_name)
        ).distinct()
        return result

    def findByNumber(self, search_number):
        result = User.objects.filter(
            Q(phnNumber__startswith=search_number)
            | Q(phnNumber__contains=search_number)
        ).distinct()
        return result

    def get(self, request):
        if "name" in request.data:
            sq = request.data["name"]
            try:
                user = UserSearch.findByName(UserSearch, sq)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

        elif "phnNumber" in request.data:
            sq = request.data["phnNumber"]
            try:
                user = UserSearch.findByNumber(UserSearch, sq)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
        if user.values("isRegistered")[0]["isRegistered"]:
            serializer = UserSearchSerializer(user, many=True)
        else:
            serializer = RegisteredUserSrializer(user, many=True)
        return Response(serializer.data)


class UserSpam(APIView):
    authentication_classes = [
        TokenAuthentication,
    ]

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        phn = request.data["phnNumber"]
        user = UserSearch.findByNumber(UserSpam, phn)
        if not user:
            serializer = SpamSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

        user.update(isSpam=True)
        serializer = SpamSerializer(user, many=True)
        return Response(serializer.data)


class getAllUserSpam(APIView):
    authentication_classes = [
        TokenAuthentication,
    ]

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        spam1 = Spam.objects.all()
        serializer = SpamSerializer(spam1, many=True)
        return Response(serializer.data)
