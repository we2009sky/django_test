from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.


def login(requests):
    if requests.method == 'GET':
        return render(requests, 'login.html')
    else:
        user = requests.POST.get('username')
        password = requests.POST.get('password')

        if user == '123' and password == '123':
            return redirect('https://www.douyu.com/g_DOTA2')
        else:
            return render(requests, 'login.html', {'msg': 'username or password error'})


def index(requests):
    return render(requests, 'index.html',
                  {
                      'name': ['user1', 'user2'],
                      'user_list_dict': [
                          {'id': 1, 'user': 'daniel', 'age': 24},
                          {'id': 2, 'user': 'haha', 'age': 24},
                          {'id': 3, 'user': 'hehe', 'age': 21}
                      ]
                  }
                  )
