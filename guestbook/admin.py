from django.contrib import admin
from .models import GuestbookEntry


@admin.register(GuestbookEntry)
class GuestbookEntryAdmin(admin.ModelAdmin):
    list_display = ('name_author', 'email_author', 'status', 'created', 'updated')
    list_filter = ('status',)
    search_fields = ('name_author', 'email_author', 'entry_text')
