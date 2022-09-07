from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from freddit.models import Thread, Comment
from freddit.forms import ThreadForm, CommentForm

# Create your views here.
def index(request):
    thread_list = Thread.objects.order_by('-likes')[:5]
    context_dict = {'threads': thread_list}
    return render(request, 'freddit/index.html', context=context_dict)

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
        context_dict['comment'] = comments        
    except Thread.DoesNotExist:
        context_dict['thread'] = None
        context_dict['comment'] = None
    return render(request, 'freddit/thread.html', context_dict)

