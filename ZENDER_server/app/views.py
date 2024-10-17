from django.shortcuts import redirect
import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_protect
from django.middleware.csrf import get_token

import hashlib
import datetime
from jwt import encode,decode

usernameDemo = "Appu"
passwordDemo = "1232"

secret = "#34Appu7&2@$$$%7767Adh3&&##sadwHUhdsdsf++===&&***??ddksdj^^5443**999?-?sdsj#333$5adf"

def getCsrfToken(request):
    # Generates and returns the CSRF token
    csrfToken = get_token(request)
    return JsonResponse({'csrfToken': csrfToken})

@csrf_protect
def auth(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            username = data['username']
            password = data['password']
            if passwordDemo == password and usernameDemo == username:
                return JsonResponse({"status": "Valid"})
            else:
                return JsonResponse({"status": "not_Valid"})
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON data")
    return HttpResponseBadRequest("Only POST requests are allowed")



def encryption(password):
    return hashlib.sha256(password.encode()).hexdigest() 

#Creating the JWT token for authentication
def auth_by_request(user_ID):
    payload = {
    'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=30),  # Expiration in 60 days
    'iat': datetime.datetime.now(datetime.timezone.utc),  # Issued at current time with UTC timezone
    'user_ID':user_ID,
}
    
    token = encode(payload,secret,algorithm = 'HS256')
    print(token)
    return token


def verify_jwt(token):
    try:
        payload = decode(token,secret,algorithms = ['HS256'])
    except KeyError as e:
        return False
    hashed_password = payload.get('password', None)
    user_name = payload.get('user_ID',None)
    print(hashed_password,user_name)

token = auth_by_request("Adwaith")
verify_jwt(token)
