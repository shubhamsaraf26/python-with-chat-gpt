from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sanity/', views.sanity, name='sanity'),
    path('health_check/', views.health_check, name='health_check'),
    path('backup_check/', views.backup_check, name='backup_check'),
]
