from django.shortcuts import render,redirect
from .models import Blogtable
from django.contrib import messages
# Create your views here.

def save_blogs(request):
    subject_name = request.POST['subject']
    contents_name = request.POST['content']
    try:
        Blogtable.objects.create(subject=subject_name,content=contents_name)
    except Exception as e:
        print(str(e))
    return redirect('dashboard_url')


def delete_blogs(request,pk):
    # Blogtable.objects.filter(id=pk).delete()
    Blogtable.objects.get(id=pk).delete()
    messages.success(request,"Data successfully deleted.") 
    return redirect('dashboard_url')