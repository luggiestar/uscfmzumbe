from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from ..models import User
from ..forms import UserForm


@login_required(login_url='/')
def users(request):
    template = 'registration/users.html'
    get_users = User.objects.all().order_by('username')
    edit_user_forms = {user.id: UserForm(instance=user) for user in get_users}

    context = {
        'users': get_users,
        'form': UserForm,
        'title': 'Users',
        'edit_user_forms': edit_user_forms
    }
    return render(request, template, context)


@login_required(login_url='/')
def delete_user(request):
    if request.method == 'POST':
        user_pk_id = request.POST['user_pk_id']
        try:
            get_user = User.objects.get(id=user_pk_id)
            get_user.delete()

            message = "User saved successfully"
            messages.success(request, message)

        except:
            message = "Something went wrong Try again"
            messages.error(request, message)

        return redirect('users')


@login_required(login_url='/')
def update_user(request):
    if request.method == 'POST':
        user_pk_id = request.POST.get('user_pk_id')
        user_instance = User.objects.get(id=user_pk_id)
        user_form = UserForm(request.POST, instance=user_instance)
        if user_form.is_valid():
            try:
                user_form.save()
                message = 'User updated successfully'
                messages.success(request, message)
            except:
                message = f'Something went wrong Try again {user_form.errors}'
                messages.error(request, message)
        else:
            message = f'{user_form.errors}Year not updated please make sure you enter valid data'
            messages.error(request, message)

    return redirect('users')
