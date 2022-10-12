from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('advertisement/', views.advertisement, name='advertisement'),
    path('add-post/', views.add_post, name='add-post'),
    path('post/<int:pk>/', views.post, name='post'),
]