from django.contrib import admin

from history.models import HistoryItem


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('reader', 'book_item', 'fine', 'is_fine_paid')
    list_filter = ('reader', 'book_item__book')
    search_fields = (
        'reader__first_name',
        'reader__last_name',
        'reader__username',
        'book_item__book__name',
        'book_item__book__author',
    )

admin.site.register(HistoryItem, HistoryAdmin)
