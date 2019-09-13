from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
import pymysql


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
    if requests.method == 'GET':
        conn = pymysql.connect(host='', user='root', password='123456', database='test', charset='utf8')
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('select id, name from user ')
        users = cursor.fetchall()
        cursor.close()
        conn.close()

        return render(requests, 'index.html', {'users': users})


def delete(requests):
    id = requests.GET.get('nid')
    conn = pymysql.connect(host='', user='root', password='123456', database='test', charset='utf8')
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute('delete from user where id=%s', [id, ])
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/index/')


def edit(requests):
    if requests.method == 'GET':
        id = requests.GET.get('nid')
        conn = pymysql.connect(host='', user='root', password='123456', database='test', charset='utf8')
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('select id, name from user where id=%s', [id, ])
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return render(requests, 'edit.html', {'result': result})
    else:
        # id = requests.POST.get('nid')
        id = requests.GET.get('nid')
        name = requests.POST.get('user')
        print(id, name)
        conn = pymysql.connect(host='', user='root', password='123456', database='test', charset='utf8')
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('update user set name=%s where id=%s', [name, id])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/index/')


def add(requests):
    if requests.method == 'GET':
        return render(requests, 'add.html')
    else:
        v = requests.POST.get('value')
        print(v)
        conn = pymysql.connect(host='', user='root', password='123456', database='test', charset='utf8')
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('insert into user(name) values (%s)', [v, ])
        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/index/')
