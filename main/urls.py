from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_view, name='main'),
    path('about/', views.about_view, name='about'),
]
