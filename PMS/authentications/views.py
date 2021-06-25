from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm

from django.contrib.auth import authenticate, login , logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages


# Create your views here.
def register(request):
    # if request.user.is_autheticated:
    #     return redirect('index')
    # else:

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created sucessfully for ' + user)
            
            return redirect ('login')

    context = {'form':form}
    return render(request, 'authentications/register.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password= password)

        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            messages.info(request, 'Username OR Password incorrect.')

    context = {}
    return render(request, 'authentications/login.html', context)


def logoutUser(request, *args, **kwargs):
    print(args, kwargs)
    auth.logout(request)
    print("LOGOUT TEMPLATE")
    print(request.user, " OUT")
    return redirect('login')
    # return render(request, 'authentications/login.html')



