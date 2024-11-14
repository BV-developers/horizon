from django.urls import path
from . import views

urlpatterns = [
    path('bv_ais/', views.BVAISView.as_view(), name='bv_ais_view'),
]