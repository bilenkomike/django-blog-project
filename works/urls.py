from django.urls import path

from . import views

urlpatterns = [
    path('', views.works, name='works'),
    path('<int:pk>/', views.work, name='work'),
]