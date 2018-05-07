from django.shortcuts import render, get_object_or_404
from .models import Entry


def index(request):
    entries = Entry.objects.all()
    return render(request, 'myapp/index.html', {'entries': entries})


def details(request, pk):
    entry = Entry.objects.get(id=pk)
    return render(request, 'myapp/details.html',  {'entry': entry})
