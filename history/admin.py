from django.contrib import admin
from history.models import HistoryItem


class HistoryAdmin(admin.ModelAdmin):
    search_fields = ('dateTaken', )

admin.site.register(HistoryItem, HistoryAdmin)
