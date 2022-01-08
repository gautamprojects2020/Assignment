from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.contrib.auth.models import Group
from django.core.paginator import Paginator

# Create your views here.
# Home
def home(request):
 posts = Post.objects.all().order_by('id')
 paginator=Paginator(posts,3)
 page_number=request.GET.get('page')
 page_obj=paginator.get_page(page_number)
 return render(request, 'debate/home.html',{'page_obj':page_obj} )

# User Profile
def user_profile(request):
    return render(request, 'debate/userprofile.html')

# Dashboard
def dashboard(request):
    return render(request, 'debate/dashboard.html', )




# Sigup
def user_signup(request):
 if request.method == "POST":
  form = SignUpForm(request.POST)
  if form.is_valid():
   messages.success(request, 'Congratulations!! You are eligible for debate. Please login to continue.')
   user = form.save()
   group = Group.objects.get(name='Debator')
   user.groups.add(group)
 else:
  form = SignUpForm()
 return render(request, 'debate/signup.html', {'form':form})

 # Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!')
                    return HttpResponseRedirect('/dashboard/')



        else:
            form = LoginForm()
            return render(request, 'debate/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


























     # form = LoginForm(request=request, data=request.POST)
     # if form.is_valid():
     #  uname = form.cleaned_data['username']
     #  upass = form.cleaned_data['password']
     #  user = authenticate(username=uname, password=upass)
     #  if user is not None:
     #   login(request, user)
     #   messages.success(request, 'Logged in Successfully !!')
     #   return HttpResponseRedirect('/dashboard/')

 #  else:
 #   form = LoginForm()
 #  return render(request, 'debate/login.html', {'form':form})
 # else:
 #  return HttpResponseRedirect('/dashboard/')

  # # Logout
  # def user_logout(request):
  #  logout(request)
  #  return HttpResponseRedirect('/')
