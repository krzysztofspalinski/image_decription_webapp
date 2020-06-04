from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Image
import requests
import json
from image_recognition_webapp import settings

@receiver(post_save, sender=Image)
def send_to_predict(sender, instance, created, **kwargs):
	if settings.SUSPEND_SIGNALS:
		return
	if created:
		data = {
				"bucket_key": str(instance),
				"image_id": str(instance.id)
				}
		json_data = json.dumps(data)
		print(data["image_id"])
		requests.post('http://internal-apploadbalancer2-820229948.eu-central-1.elb.amazonaws.com:5000/image_upload', data=data)
