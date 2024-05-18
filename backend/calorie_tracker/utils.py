import os
import base64
import bcrypt
from django.utils import timezone
from datetime import timedelta

def generate_session_cookie(length=32):
    random_bytes = os.urandom(length)
    base64_string = base64.urlsafe_b64encode(random_bytes).decode('utf-8')
    return base64_string

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def clear_session(user):
    user.session_cookie = None
    user.session_expiration = None
    user.save()

def set_session_cookie(user, duration_hours=24):
    user.session_cookie = generate_session_cookie()
    user.session_expiration = timezone.now() + timedelta(hours=duration_hours)
    user.save()
    return user.session_cookie

def is_session_valid(user):
    if user.session_expiration and timezone.now() < user.session_expiration:
        return True
    return False


