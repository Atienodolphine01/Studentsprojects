from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required



def home(request):
    projects = Projects.objects.all()
    context = {
        "projects":projects,
    }
    return render(request,'index.html', context)


@login_required
def updateprofile(request):
    projects = Projects.objects.all()
    posts = Profile.objects.all()
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated successfully')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form':user_form,
        'profile_form':profile_form,
        'posts':posts,
        'projects':projects,
    }
    return render(request, 'updateprof.html', context)



@login_required
def profile(request):
    projects = Projects.objects.all()
    posts = Profile.objects.all()
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated successfully')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
    'user_form':user_form,
    'profile_form':profile_form,
    'posts':posts,
    'projects':projects,
    }
    return render(request, 'profile.html', context)




def postproject(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = current_user
            project.save()
        return redirect('/')
    else:
        form = ProjectForm()
    context = {
        'form':form,
    }
    return render(request, 'createproject.html', context)

def get_project(request, id):
    project = Projects.objects.get(pk=id)

    return render(request, 'project.html', {'project':project})
    


@login_required
def search_projects(request):
    if 'post' in request.GET and request.GET['post']:
        search_term = request.GET['post']
        searched_projects = Projects.search_projects(search_term)
        message = f'search_term'

        context ={
            "projects":searched_projects,
            "message":message
        }
        return render(request, 'search.html', context)
    else:
        message = "No user has been searched"
        context = {
            "message":message,
        }
        return render(request, 'search.html', context)


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect('/login')
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'users/register.html', context)


class ProfileList(APIView):
    def get(self,request, format=None):
        allprofiles = Profile.objects.all()
        serializers = ProfileSerializer(allprofiles, many=True)
        return Response(serializers.data)



class ProjectList(APIView):
    def get(self, request, format=None):
        allprojects = Projects.objects.all()
        serializers = ProjectSerializer(allprojects, many=True)
        return Response(serializers.data)