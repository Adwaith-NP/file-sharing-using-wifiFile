from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_protect
from django.middleware.csrf import get_token

usernameDemo = "Appu"
passwordDemo = "1232"

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



def getCsrfToken(request):
    # Generates and returns the CSRF token
    csrfToken = get_token(request)
    return JsonResponse({'csrfToken': csrfToken})
