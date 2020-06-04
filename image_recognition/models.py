from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Image(models.Model):
	user_description = models.TextField()
	model_description = models.TextField(blank=True, null=True)
	description_ready = models.BooleanField(default=False)
	original_image = models.ImageField(default=None, upload_to='original_images')
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.original_image)

	def get_absolute_url(self):
		return reverse('image-detail', kwargs={'pk': self.pk})

class ImageAttentionDescription(models.Model):
	image = models.ForeignKey(Image, on_delete=models.CASCADE)
	attention_image = models.ImageField(default=None, upload_to='attention_images')
	attention_word = models.TextField()