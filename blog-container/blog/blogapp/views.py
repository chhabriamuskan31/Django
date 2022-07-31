from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection 

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Hello world</h1>")
    # return render(request,'blogapp/home.html');
    cursor = connection.cursor()
    cursor.execute('SELECT * from posts where softdelete = 0')

    columns = [col[0] for col in cursor.description]
    posts =  [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    context = {
        'keyposts': posts
    }
    return render(request,'blogapp/home.html',context)

def create(request):
    return render(request, 'blogapp/form.html')

def insert(request):
    title = request.POST['blogTitle']
    content = request.POST['content']
    cursor = connection.cursor()
    cursor.execute("INSERT INTO posts (`title`,`content`) VALUES ( %s, %s );", (title, content))
    return redirect('/blog/home')

