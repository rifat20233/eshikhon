from django.urls import path
from .views import save_blogs,delete_blogs



urlpatterns = [
    path('save_blogs/',save_blogs,name='save_blogs_function'),
    path('delete_blogs/<int:pk>',delete_blogs,name='delete_blogs_function'),
]
