from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blogs.models import Blogtable

# Create your views here.
@login_required(login_url='/')
def dashboard(request):
    querydata = Blogtable.objects.all()
    context = {
        'table_data' : querydata
    }
    return render(request,'dashboard_index.html',context)