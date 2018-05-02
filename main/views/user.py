from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.models import User
from main.models import User

def checkuser(request):
    if request.method = 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')

        try:
            password_db = User.objects.get(username=user).password
        except:
            messages.add_message(request, messages.WARNNING, '找不到用户')
            return render(request, '')
