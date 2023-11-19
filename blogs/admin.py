from django.contrib import admin
from .models import Blogtable
# Register your models here.

class ShowFields(admin.ModelAdmin):
    list_display = ('id','subject','content','created_at')
    search_fields = ('subject',)

admin.site.register(Blogtable,ShowFields)