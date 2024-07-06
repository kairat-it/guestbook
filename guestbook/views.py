from django.shortcuts import render, redirect, get_object_or_404
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

def edit_entry(request, entry_id):
    entry = get_object_or_404(GuestbookEntry, pk=entry_id)
    if request.method == 'POST':
        form = GuestbookEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GuestbookEntryForm(instance=entry)
    return render(request, 'guestbook/edit_entry.html', {'form': form})

def delete_entry(request, entry_id):
    entry = get_object_or_404(GuestbookEntry, pk=entry_id)
    if request.method == 'POST':
        email = request.POST.get('email')
        if email == entry.email_author:
            entry.delete()
            return redirect('index')
        else:
            error = "Неверная почта."
            return render(request, 'guestbook/delete_entry.html', {'entry': entry, 'error': error})
    return render(request, 'guestbook/delete_entry.html', {'entry': entry})
