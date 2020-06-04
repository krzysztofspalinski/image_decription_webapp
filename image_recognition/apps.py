from django.apps import AppConfig


class ImageRecognitionConfig(AppConfig):
    name = 'image_recognition'

    def ready(self):
    	import image_recognition.signals