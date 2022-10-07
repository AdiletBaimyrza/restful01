from django.urls import path, re_path
from . import views

urlpatterns = [
    path('toys/', views.toy_list),
    path('toys/<int:pk>/', views.toy_detail)
]
