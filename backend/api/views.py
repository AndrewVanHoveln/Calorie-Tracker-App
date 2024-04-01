from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, FoodEntrySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import FoodEntry

# Create your views here.

class FoodListCreate(generics.ListCreateAPIView):
    serializer_class = FoodEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return FoodEntry.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class FoodDelete(generics.DestroyAPIView):
    serializer_class = FoodEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return FoodEntry.objects.filter(author=user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]