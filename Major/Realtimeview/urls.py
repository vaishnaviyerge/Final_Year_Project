from django.urls import path
from . import views

urlpatterns = [
    path('Realtimeview/', views.Realtimeview, name='realtimeview'),
]
