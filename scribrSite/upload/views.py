from django.shortcuts import render, redirect
from .forms import VideoUploadForm
from .models import Video

def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoUploadForm()
    return render(request, 'upload_video.html', {'form': form})

def video_list(request):
    videos = Video.objects.all()
    for video in videos:
        print(video.title, video.video_file.url)
    return render(request, 'video_list.html', {'videos': videos})

def homepage(request):
    return render(request, 'homepage.html')
# Create your views here.
