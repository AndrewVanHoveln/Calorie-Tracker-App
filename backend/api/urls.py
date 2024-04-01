from django.urls import path
from . import views

urlpatterns = [
    path('entries/', views.FoodListCreate.as_view(), name = 'food-list'),
    path('notes/delete/<int:pk>/', views.FoodDelete.as_view(), name = 'delete-food'),
]