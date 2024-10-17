import requests
csrftoken = None
csrftoken_url = "http://127.0.0.1:8000/ZENDER-API/getCsrfToken/"
authentication_url = "http://127.0.0.1:8000/ZENDER-API/authentication/"


def auth_user(username,password):
    try:
        session = requests.Session()
        response = session.get(csrftoken_url)
        csrftoken = session.cookies.get('csrftoken')
    except:
        return False
        
    if csrftoken:
        data = {
            "username": username,
            "password": password,
        }
        headers = {
            "X-CSRFToken": csrftoken 
        }
        response = session.post(authentication_url, json=data, headers=headers)
        if response.status_code == 200:
            res = response.json()['status']
            if res == "Valid":
                return True
    
    return False
