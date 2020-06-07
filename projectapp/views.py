from django.shortcuts import render
from .models import *


def home(request):
    projects = Projects.objects.all()
    context = {
        "projects":projects,
    }
    return render(request,'index.html', context)