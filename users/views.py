from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'post':
        form = UserRegisterForm()
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.sucess(request, f'Account Created Sucessfully, {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
