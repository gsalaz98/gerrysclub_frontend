from django.contrib.auth import login
from django.shortcuts import redirect

def auth_login(request):
    if request.user.is_authenticated:
        return redirect('/')

    return login(request)
