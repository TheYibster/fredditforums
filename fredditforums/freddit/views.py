from http.client import HTTPResponse
from django.shortcuts import render, redirect
from freddit.models import Thread, Comment
from freddit.forms import ThreadForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    thread_list = Thread.objects.order_by('-likes')[:5]
    context_dict = {'threads': thread_list}
    return render(request, 'freddit/index.html', context=context_dict)

def add_comment(request, thread_slug):
    try:
        thread = Thread.objects.get(slug=thread_slug)
    except Thread.DoesNotExist:
        thread = None
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            if thread:
                comment = form.save(commit=False)
                comment.thread = thread
                comment.likes = 0
                comment.save()
                return view_thread(request, thread_slug)
        else:
            print(form.errors)
    return render(request, 'freddit/add_comment.html', {'comment': form, 'thread': thread})

def add_thread(request):
    form = ThreadForm()
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    return render(request, 'freddit/add_thread.html', {'form': form})

def view_thread(request, thread_slug):
    context_dict = {}
    try:
        thread = Thread.objects.get(slug=thread_slug)
        comments = Comment.objects.filter(thread=thread)
        context_dict['thread'] = thread
        context_dict['comments'] = comments        
    except Thread.DoesNotExist:
        context_dict['thread'] = None
        context_dict['comments'] = None
    return render(request, 'freddit/thread.html', context_dict)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ('There was an error, try again.'))
            return redirect('login_user')
    else:
        return render(request, 'authentication/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You are now logged out."))
    return redirect('index')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful"))
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register_user.html', {'form': form})