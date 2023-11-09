from django.test import TestCase
from django.urls import reverse
from cake.tests import factories
from cake import models


class TestCakesView(TestCase):
    def test_get_cakes(self):
        cake = factories.CakeFactory()
        response = self.client.get(reverse("cakes"))
        self.assertEqual(response.status_code, 200)
        expected_response = [
            {
                "id": cake.id,
                "name": cake.name,
                "comment": cake.comment,
                "yumFactor": cake.yum_factor,
                "imageUrl": cake.image_url,
            }
        ]
        self.assertEqual(response.json(), expected_response)

    def test_create_cake(self):
        post_data = {
            "name": "Chocolate Cake",
            "comment": "A rich chocolate cake",
            "yumFactor": 5,
            "imageUrl": "https://www.google.com",
        }
        response = self.client.post(
            reverse("cakes"), data=post_data, content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        cake = models.Cake.objects.first()
        self.assertEqual(cake.name, post_data["name"])
        self.assertEqual(cake.comment, post_data["comment"])
        self.assertEqual(cake.yum_factor, post_data["yumFactor"])
        self.assertEqual(cake.image_url, post_data["imageUrl"])
        post_data["id"] = cake.id
        self.assertEqual(response.json(), post_data)

    def test_create_cake_with_invalid_data(self):
        post_data = {
            "name": "Chocolate Cake wuth a realllllllllly long name",
            "comment": "A rich chocolate cake",
            "yumFactor": 9999,
        }
        response = self.client.post(
            reverse("cakes"), data=post_data, content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(models.Cake.objects.count(), 0)
        expected_errors = {
            "name": ["Ensure this field has no more than 30 characters."],
            "yumFactor": ["YumFactor must be between 1 and 5"],
            "imageUrl": ["This field is required."],
        }
        self.assertEqual(response.json(), expected_errors)


class TestCakeView(TestCase):
    def setUp(self) -> None:
        self.cake = factories.CakeFactory()
        self.cake_detail_url = reverse("cake", kwargs={"pk": self.cake.id})

    def test_get_cake_detail(self):
        response = self.client.get(self.cake_detail_url)
        self.assertEqual(response.status_code, 200)
        expected_response = {
            "id": self.cake.id,
            "name": self.cake.name,
            "comment": self.cake.comment,
            "yumFactor": self.cake.yum_factor,
            "imageUrl": self.cake.image_url,
        }
        self.assertEqual(response.json(), expected_response)

    def test_delete_cake(self):
        response = self.client.delete(self.cake_detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(models.Cake.objects.count(), 0)
