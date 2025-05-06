from django.shortcuts import render

def Realtimeview(request):
    return render(request, 'Realtimeview.html', {
    'video_url': '/static/website_to_dive.mp4'
    })