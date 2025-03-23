from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ..forms import ChangePasswordForm
from ..models import User


def login_view(request):
    template = 'auth/login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect('dashboard')
            else:
                return redirect('dashboard')
        else:
            error_message = 'Invalid username or password'
            messages.error(request, error_message)
            return redirect('login')

    return render(request, template)


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/')
def change_password_view(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)

        if form.is_valid():
            current_password = form.cleaned_data['current_password']
            new_password = form.cleaned_data['new_password']
            confirm_password = form.cleaned_data['confirm_password']

            staff_instance = User.objects.get(id=request.user.id)

            if new_password == confirm_password:
                if staff_instance.check_password(current_password):
                    staff_instance.set_password(new_password)
                    staff_instance.save()
                    messages.success(request, 'Password changed successfully.')
                    return redirect('change_password')
                else:
                    messages.error(request, 'Current password is incorrect.')
                    return redirect('change_password')
            else:
                messages.error(request, 'New password and Confirm password must be the same')
                return redirect('change_password')
    return render(request, 'auth/change-password.html', context={'form': ChangePasswordForm})