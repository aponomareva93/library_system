from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render_to_response, render


def home(request):
    return render_to_response('index.html', {'username': request.user.first_name})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password changed.")
            return render(request, "change_pass.html",
                          {'form': PasswordChangeForm(request.user), 'message': messages})
        else:
            messages.error(request, "Incorrect password")
            return render(request, "change_pass.html",
                          {'form': PasswordChangeForm(request.user), 'message': messages})
    return render(request, "change_pass.html",
                  {'form': PasswordChangeForm(request.user), 'message': messages})
