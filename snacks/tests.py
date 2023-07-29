from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth.models import User
from django.test.client import Client

from .models import Snack,Post
# Create your tests here.
class SnackTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="moath_1", password="marena1"
        )
        testuser1.save()

        testuser2 = get_user_model().objects.create_user(
            username="moath_2", password="marena2"
        )
        testuser2.save() 

        testuser3 = get_user_model().objects.create_superuser(
            username="moath", password="marena"
        )
        testuser3.save() 

        # my_superuser = User.objects.create_superuser('moath', 'myemail@test.com', 'marena')
        # c = Client()
        # # You'll need to log him in before you can send requests through the client
        # c.login(username=my_superuser.username, password='marena')

    

        test_snack = Snack.objects.create(
            name="chips",
            owner=testuser1,
            desc="salty",
        )
        test_snack.save()

    def setUp(self) -> None:
         self.client.login(username="moath_1", password="marena1")  

   
    def test_snacks_model(self):
        snack = Snack.objects.get(id=1)
        actual_owner = str(snack.owner)
        actual_name = str(snack.name)
        actual_desc = str(snack.desc)
        self.assertEqual(actual_owner, "moath_1")
        self.assertEqual(actual_name, "chips")
        self.assertEqual(
            actual_desc, "salty"
        )

    def test_get_snacks_list(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snacks = response.data
        self.assertEqual(len(snacks), 1)
        self.assertEqual(snacks[0]["name"], "chips")


    def test_if_normal_user_can_post(self):
        self.client.logout()
        self.client.login(username="moath_1", password="marena1")
        url = reverse("snack_list")  
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_normal_user_can_delete(self):
        self.client.logout()
        self.client.login(username="moath_1", password="marena1")
        url = reverse("snack_detail",args=[1])  
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

