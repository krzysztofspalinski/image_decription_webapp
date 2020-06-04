from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
from django.urls import reverse

class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="UnittestTestUser1")
        self.user1 = User.objects.filter(username="UnittestTestUser1").first()
        

    def tearDown(self):
    	self.user1.delete()
    	# user 2 was deleted in deleting_

    def test_creating_user_creates_profile(self):
        self.assertTrue(len(Profile.objects.filter(user_id=self.user1.id)) == 1)
        


    def test_deleting_user_delets_its_profile(self):
    	User.objects.create(username="UnittestTestUser2")
    	user2 = User.objects.filter(username="UnittestTestUser2").first()

    	user2_id = user2.id
    	user2.delete()

    	self.assertTrue(len(Profile.objects.filter(user_id=user2_id)) == 0)

    def test_anonymous_cant_see_profile(self):
        response = self.client.get(reverse('profile'))
        self.assertRedirects(response, "/login/?next=/profile/")