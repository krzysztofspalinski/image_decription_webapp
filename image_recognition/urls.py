from django.urls import path
from . import views
from .views import (
	ImageListView,
	ImageDetailView, 
	ImageCreateView, 
	ImageDeleteView,
	UserImageListView)

urlpatterns = [
	path('', ImageListView.as_view(), name='image_recognition-home'),
	path('user-images/', UserImageListView.as_view(), name='user-images'),
	path('image/<int:pk>/', ImageDetailView.as_view(), name='image-detail'),
	path('image/<int:pk>/delete/', ImageDeleteView.as_view(), name='image-delete'),
	path('image/new/', ImageCreateView.as_view(), name='image-create'),
	path('about/', views.about, name='image_recognition-about'),
]