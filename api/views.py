from django.shortcuts import render
from image_recognition.models import ImageAttentionDescription, Image
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponseNotFound
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError


@csrf_exempt
def add_description(request):
	if request.method == "POST":
		data = request.POST
		data = dict(data)
		secret_key = str(data.get('secret_key', '')[0])
		image_id = int(data['image_id'][0])

		
		# if str(secret_key) == os.environ.get('AWS_SECRET_ACCESS_KEY'):
		if str(secret_key) == "87654321":
			try:
				full_description = ''
				for index in range(0, len(data["text"])):
					image_name = str(data["pictures"][index])
					described_word = str(data["text"][index])
					full_description = full_description + described_word + ' '
					ImageAttentionDescription.objects.create(image_id=image_id, attention_image=image_name, attention_word=described_word)
				image = Image.objects.filter(id=image_id).first()
				image.model_description = full_description
				image.description_ready = True
				image.save()
				return JsonResponse({'Success': 'True'})
			except KeyError as e:
				return JsonResponse({'error': str(e)})
	else:
		return JsonResponse({'error': f"Request method not supported: {request.method}"})
