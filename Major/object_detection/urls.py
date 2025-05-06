from django.urls import path
from . import views

urlpatterns = [
    path('', views.object_detection, name='object_detection'),
    path('history/', views.history, name='object_detection_history'),
    path('delete/<str:pk>', views.delete, name='object_detection_delete'),
]