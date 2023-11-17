from django.contrib import admin
from .models import Blogtable
# Register your models here.

class ShowFields(admin.ModelAdmin):
    list_display = ('id','subject','content')
    search_fields = ('subject',)

admin.site.register(Blogtable,ShowFields)