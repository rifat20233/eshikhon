from django.urls import path
from .views import *



urlpatterns = [
    path('save_blogs/',save_blogs,name='save_blogs_function'),
    path('delete_blogs/<int:pk>',delete_blogs,name='delete_blogs_function'),
    path('update_blogs/<int:pk>',update_html,name='update_blogs_function'),
]
