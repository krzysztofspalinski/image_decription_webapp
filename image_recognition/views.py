from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
	ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Image


def home(request):
	context = {
		'images': Image.objects.all()
	}
	return render(request, 'blog/home.html', context)

class ImageListView(ListView):
	model = Image
	template_name = 'image_recognition/home.html'
	context_object_name = 'images'
	ordering = ['-date_posted']
	paginate_by = 5


class UserImageListView(LoginRequiredMixin, ListView):
	model = Image
	template_name = 'image_recognition/user_images.html'
	context_object_name = 'images'
	ordering = ['-date_posted']
	paginate_by = 5

	def get_queryset(self):
		user = self.request.user
		return Image.objects.filter(author=user).order_by('-date_posted')


class ImageDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
	model = Image

	def test_func(self):
		image = self.get_object()
		if self.request.user == image.author:
			return True
		else:
			return False

class ImageCreateView(LoginRequiredMixin, CreateView):
	model = Image
	fields = ['user_description', 'original_image']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class ImageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Image
	success_url = '/'

	def test_func(self):
		image = self.get_object()
		if self.request.user == image.author:
			return True
		else:
			return False


def about(request):
	context = {
		'title': 'About Section'
	}
	return render(request, 'image_recognition/about.html', context)