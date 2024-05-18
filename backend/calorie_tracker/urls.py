from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),
    path("add-entry", views.addEntry, name='add-entry'),
    path("delete-entry", views.deleteEntry, name='delete-entry'),
    path("modify-entry", views.modifyEntry, name='modify-entry'),
    path("register", views.register, name='register'),
    path('get-entries', views.getEntries, name='get-entries')
]
