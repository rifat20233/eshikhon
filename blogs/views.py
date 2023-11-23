from django.shortcuts import render,redirect
from .models import Blogtable
from django.contrib import messages
# Create your views here.

def save_blogs(request):
    subject_name = request.POST['subject']
    contents_name = request.POST['content']
    image_data = request.FILES['image_upload']
    try:
        Blogtable.objects.create(subject=subject_name,content=contents_name,imageField=image_data)
    except Exception as e:
        print(str(e))
    return redirect('dashboard_url')


def delete_blogs(request,pk):
    # Blogtable.objects.filter(id=pk).delete()
    Blogtable.objects.get(id=pk).delete()
    messages.success(request,"Data successfully deleted.") 
    return redirect('dashboard_url')


def update_html(request,pk):
        if request.method == "POST":
            subject_name = request.POST['subject']
            contents_name = request.POST['content']
            try:
                # db_data = Blogtable.objects.get(id=pk)
                # db_data.subject = subject_name
                # db_data.content = contents_name
                # db_data.save()
                Blogtable.objects.filter(id=pk).update(subject=subject_name,content=contents_name)
                messages.success(request,"data succesfully updated.")
            except Exception as e:
                print(str(e))
                messages.error(request,str(e))

            return redirect('dashboard_url')
        else:
             context = {}
        try:
            db_data = Blogtable.objects.get(id=pk)
            context['data'] = db_data
        except Exception as e:
            messages.error(request,str(e))
        return render(request,'update_data.html',context)