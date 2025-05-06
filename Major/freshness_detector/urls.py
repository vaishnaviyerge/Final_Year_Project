from django.urls import path
from . import views 

urlpatterns = [
    path('', views.freshness_detector, name='freshness_detector'),
    path('history/', views.history, name='freshness_detector_history'),
    path('delete/<str:pk>/', views.delete, name='freshness_detector_delete'),
]
