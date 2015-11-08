from django.shortcuts import render_to_response
from history.models import HistoryItem


def view_book_list(request):
    try:
        reader_history = HistoryItem.objects.filter(reader_id=request.user.pk)
        total_fine = 0
        for item in reader_history:
            if item.fine > 0 and not item.isFinePaid:
                total_fine = total_fine + item.fine
    except:
        reader_history = []
    return render_to_response('book_list.html', {'books': reader_history, 'total_fine': total_fine})
