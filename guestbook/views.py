from django.shortcuts import render
from .models import GuestbookEntry


def index(request):
    entries = GuestbookEntry.objects.filter(status='active')
    return render(request, 'guestbook/index.html', {'entries': entries})
