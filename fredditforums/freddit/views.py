from http.client import HTTPResponse
from django.shortcuts import render
from freddit.models import Thread
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
