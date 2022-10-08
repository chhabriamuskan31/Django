from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection 

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello world</h1>")
    #  return render(request,'newapp/home.html');
    # cursor = connection.cursor()
    # cursor.execute('SELECT * from posts where softdelete = 0')

    # columns = [col[0] for col in cursor.description]
    # posts =  [
    #     dict(zip(columns, row))
    #     for row in cursor.fetchall()
    # ]
    # context = {
    #     'keyposts': posts
    # }
    # return render(request,'newapp/home.html',context)

def create(request):
    return render(request, 'newapp/form.html')

def insert(request):
    title = request.POST['newTitle']
    content = request.POST['content']
    cursor = connection.cursor()
    cursor.execute("INSERT INTO posts (`title`,`content`) VALUES ( %s, %s );", (title, content))
    return redirect('/new/home')

