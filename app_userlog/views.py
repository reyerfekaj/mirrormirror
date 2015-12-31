from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext

# Create your views here.
 
@csrf_protect
def login_page(request):
    return login(request, template_name='userlog/login.html')   

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            #return HttpResponseRedirect('/register/success/')
            return redirect('register_success')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'userlog/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'userlog/success.html',
    )
 
@login_required
def logout_page(request):
    logout(request)
    #return HttpResponseRedirect('/')
    return redirect('login_page')
 
@login_required
def home(request):
    # dual purpose: create user profile and get username
    username = request.user.profile.user.username
    print(username)
    return render_to_response(
    'userlog/home.html',
    { 'user': username }
    )

def info(request):
    return render(request, "userlog/info.html", {})
