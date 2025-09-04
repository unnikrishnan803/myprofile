from django.shortcuts import render, redirect
from .models import Vlog, Project, Content

# Create your views here.
def index(request):
    content = {c.key: c.value for c in Content.objects.all()}
    return render(request, 'index.html', {'content': content})

def vlogs(request):
    vlogs = Vlog.objects.all().order_by('-created_at')
    return render(request, 'vlogs.html', {'vlogs': vlogs})

def projects(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'projects.html', {'projects': projects})
