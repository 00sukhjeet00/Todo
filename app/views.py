from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app.forms import TodoForm
from app.models import Todo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


def signin(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'signin.html', context)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            context = {'form': form}
            return render(request, 'signin.html', context)


def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'signup.html', context)
    else:
        form = UserCreationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('signin')
        else:
            return render(request, 'signup.html', context)


@login_required(login_url='signin')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TodoForm()
        todos = Todo.objects.filter(user=user)
        return render(request, 'home.html', context={'form': form, 'todos': todos})


@login_required(login_url='signin')
def addTodo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('home')
        else:
            return render(request, 'index.html', context={'form': form})


def signout(request):
    logout(request)
    return redirect('signin')


def delete(request, title):
    Todo.objects.get(title=title).delete()
    return redirect('home')


def change(request, title):
    check = Todo.objects.get(title=title)
    if check.status == 'P':
        check.status = 'C'
        check.save()
        return redirect('home')
    else:
        return redirect('home')


def deleteAccount(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        User.objects.get(username=user).delete()
        return redirect('index')
