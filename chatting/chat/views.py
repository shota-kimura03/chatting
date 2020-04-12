from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def indexfunc(request):
    return render(request, 'chat/index.html', {})

def roomfunc(request, room_name1, room_name2):
    print(room_name1, room_name2)
    if room_name1 > room_name2:
        room_name = str(room_name2) + str(room_name1)
    else:
        room_name = str(room_name1) + str(room_name2)

    user = User.objects.get(pk=room_name1)
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'send_id': room_name1,
        'recv_id': room_name2,
        'user_name': user
    })

def listfunc(request):
    user = User.objects.exclude(pk=request.user.pk)
    return render(request, 'chat/list.html', {
        'objects': user,
        'current_user': request.user.pk
    })

def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'chat/login.html', {'error': 'ログインIDかパスワードが間違ってます'})
    return render(request, 'chat/login.html')

def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.get(username=username)
            return render(request, 'chat/signup.html', {'error': 'このログインIDは登録されています'})
        except:
            pass
        User.objects.create_user(username, '', password)
        return redirect('login')
    return render(request, 'chat/signup.html')