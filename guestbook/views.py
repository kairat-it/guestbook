from django.shortcuts import render, redirect
from .models import GuestbookEntry
from .forms import GuestbookEntryForm


def index(request):
    entries = GuestbookEntry.objects.filter(status='active')
    return render(request, 'guestbook/index.html', {'entries': entries})

def add_entry(request):
    if request.method == 'POST':
        form = GuestbookEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GuestbookEntryForm()
    return render(request, 'guestbook/add_entry.html', {'form': form})
