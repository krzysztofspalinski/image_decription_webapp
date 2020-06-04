from django.urls import path
from .views import add_description

app_name = "api"

urlpatterns = [
	path('add_description/', add_description, name='add-description'),
]