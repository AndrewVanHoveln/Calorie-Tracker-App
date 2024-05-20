from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),
    path("add", views.addEntry, name='add-entry'),
    path("<int:id>/delete", views.deleteEntry, name='delete-entry'),
    path("<int:id>/modify", views.modifyEntry, name='modify-entry'),
    path("register", views.register, name='register'),
    path('get', views.getEntries, name='get-entries')
]
