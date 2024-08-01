# video_uploader/urls.py
from django.urls import path
from .views import upload_video, video_list

urlpatterns = [
    path('upload/', upload_video, name='upload_video'),  # This should match the view you want to access
    path('videos/', video_list, name='video_list'),
]
