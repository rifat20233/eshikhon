from django.shortcuts import render,redirect
from .models import Blogtable
# Create your views here.

def save_blogs(request):
    subject_name = request.POST['subject']
    contents_name = request.POST['content']
    try:
        Blogtable.objects.create(subject=subject_name,content=contents_name)
    except Exception as e:
        print(str(e))
    return redirect('dashboard_url')