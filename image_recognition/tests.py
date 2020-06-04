from django.test import TestCase
from users.models import Profile
from django.contrib.auth.models import User
from image_recognition.models import Image, ImageAttentionDescription
from django.urls import reverse

class ImageTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="UnittestTestUser1")
        self.user1 = User.objects.filter(username="UnittestTestUser1").first()
        

    def test_deleting_image_deletes_its_description(self):
        Image.objects.create(author=self.user1, original_image="TEST_IMAGE.jpg", user_description="Test description 2")
        image = Image.objects.filter(author=self.user1, user_description="Test description 2").first()
        ImageAttentionDescription.objects.create(image_id = image.id, attention_image="TEST_IMAGE.jpg", attention_word="some_word")
        image.delete()
        self.assertTrue(len(ImageAttentionDescription.objects.filter(image_id = image.id, attention_image="TEST_IMAGE.jpg", attention_word="some_word").all()) == 0)

    def test_anonymous_cant_see_pictures(self):
        response = self.client.get(reverse('user-images'))
        self.assertRedirects(response, "/login/?next=/user-images/")

    def test_anonymous_cant_see_picture_detail(self):
        response = self.client.get(reverse('image-detail', kwargs={'pk': '1'}))
        self.assertRedirects(response, "/login/?next=/image/1/")

    def test_deleting_user_delets_his_images(self):
        user1_id = self.user1
        Image.objects.create(author=self.user1, original_image="TEST_IMAGE.jpg", user_description="Test description 3")
        self.user1.delete() 
        self.assertTrue(len(Image.objects.filter(author=user1_id).all()) == 0)



        