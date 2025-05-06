from django.urls import path
from . import views

urlpatterns = [
    path('', views.feature_extractor, name='feature_extractor'),
    path('history/', views.history, name='feature_extractor_history'),
    path('delete/<str:pk>', views.delete, name='feature_extractor_delete'),
]