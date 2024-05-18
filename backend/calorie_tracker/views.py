from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import utils
import json
from .models import User, Entry
import datetime

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def home(request):
    return Response("Welcome to the base address")

@api_view(['POST'])
def login(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username)
        if not user.exists():
            return Response("Usename Does Not Exist", status=401)

        user = user.first()
        if not utils.check_password(password, user.password):
            return Response("Incorrect Password", status=402)
        session_id = utils.set_session_cookie(user)

        return Response(session_id)
        
    except json.JSONDecodeError:
        return HttpResponse("Invalid Data", status=400)

@api_view(['POST'])
def register(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = utils.hash_password(data.get('password'))

        if not username or not password:
            return JsonResponse({'error': 'Username and password are required'}, status=400)

        if User.objects.filter(username=username).exists():
            return HttpResponse("Usename Exists", status=401)
        user = User(username=username, password=password)
        user.save()
        return HttpResponse('User created successfully')

    except json.JSONDecodeError:
        return HttpResponse("Invalid Data", status=400)
    

@api_view(['POST'])
def logout(request):
    try:
        data = json.loads(request.body)
        session_id = data.get('session_cookie')
        if not session_id:
            return Response("Invalid Input", status=401)
        user = User.objects.filter(session_cookie=session_id)

        if not user:
            return Response("Session Does Not Exist", status=401)
        user = user.first()

        utils.clear_session(user)
        return Response("Sucessful Logout")
    except json.JSONDecodeError:
        return HttpResponse("Invalid Data", status=400)
    
logout_request = Response("logout", status=303)

@api_view(['POST'])
def addEntry(request):
    try:
        data = json.loads(request.body)
        session_id = data.get('session_cookie')
        if not session_id:
            return Response("Invalid Input", status=401)
        user = User.objects.filter(session_cookie=session_id)

        if not user:
            return Response("Session Does Not Exist", status=401)
        user = user.first()

        if not utils.is_session_valid(user):
            utils.clear_session(user)
            return logout_request

        date = data.get('date')
        date = datetime.date.fromisoformat(date)
        food = data.get('food')
        protein = data.get('protein')
        carbohydrates = data.get('carbohydrates') 
        fats = data.get('fats')
        if not (date and food and protein and carbohydrates and fats):
            return Response("Invalid Input", status=400)
        
        entry = Entry(user=user, date=date, food=food, protein=protein, carbohydrates=carbohydrates, fats=fats)
        entry.save()
        return Response("Entry Saved Sucessfully", status=200)

    except json.JSONDecodeError:
        return HttpResponse("Invalid Data", status=400)

@api_view(['POST'])
def deleteEntry(request):
    return HttpResponse("Welcome to the base address")

@api_view(['POST'])
def modifyEntry(request):
    return HttpResponse("Welcome to the base address")

@api_view(['GET'])
def getEntries(request):
    try:
        data = json.loads(request.body)

        session_id = data.get('session_cookie')
        if not session_id:
            return Response("Invalid Input", status=401)
        
        user = User.objects.filter(session_cookie=session_id)
        if not user:
            return Response("Session Does Not Exist", status=401)
        user = user.first()

        if not utils.is_session_valid(user):
            utils.clear_session(user)
            return logout_request
        
        entries = Entry.objects.filter(user=user)

        serialized_entries = [{'id': entry.id, 'date': entry.date, 'food': entry.food, 'protein': entry.protein,
                                'carbohydrates': entry.carbohydrates, 'fats': entry.fats} for entry in entries]
        return Response(serialized_entries)
        
    except json.JSONDecodeError:
        return HttpResponse("Invalid Data", status=400)
