from email import contentmanager
from turtle import title
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from .models import Blog  
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Hello world</h1>")
    # return render(request,'blogapp/home.html');
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
    # return render(request,'blogapp/home.html',context)

    posts = Blog.objects.filter(softDelete=0)
    print(posts)
    context={
        'keyposts':posts
    }
    return render(request,'blogapp/home.html',context)

def create(request):
    return render(request, 'blogapp/form.html')

def insert(request):
    title = request.POST['blogTitle']
    content = request.POST['content']
    file = request.FILES['imgageFile']
    # cursor = connection.cursor()
    # cursor.execute("INSERT INTO posts (`title`,`content`) VALUES ( %s, %s );", (title, content))
    blog = Blog(title=title, content=content, file=file)
    blog.save()
    return redirect('/blog/home')
    

def edit(request, pk):
    print(pk)
    # cursor = connection.cursor()
    # cursor.execute(f'SELECT * from posts where softdelete = 0 and id = {pk}')

    # # A list of dictionary
    # columns = [col[0] for col in cursor.description]
    # posts =  [
    #     dict(zip(columns, row))
    #     for row in cursor.fetchall()
    # ]
    posts=Blog.objects.get(id=pk)
    context = {
        'keyposts': posts
    }
    print(context)
    return render(request,'blogapp/editform.html',context)


def update(request):
    id = request.POST['id']
    title= request.POST['blogTitle']
    content = request.POST['content']
    # cursor = connection.cursor()
    # # print(title, content, id)
    # cursor.execute("UPDATE posts set title = %s ,content= %s where id = %s", (title, content, id))
    # cursor = connection.cursor()
    blog=Blog.objects.get(id=id)
    blog.title=title
    blog.content=content
    blog.save()

    return redirect('/blog/home')

@login_required
def profile(request):
    return render(request,'blogapp/profile.html')

def delete(request,pk):
    # cursor = connection.cursor()
    # # print(title, content, id)
    # cursor.execute(f'UPDATE posts set softdelete = 1 where id={pk}')
    blog = Blog.objects.get(id=pk)
    blog.softDelete = 1
    blog.save()
    return redirect('/blog/home')
