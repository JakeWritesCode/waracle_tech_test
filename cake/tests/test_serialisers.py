from rest_framework.exceptions import ErrorDetail

from cake import serialisers
from cake.tests import factories
from django.test import TestCase


class TestCakeSerialiser(TestCase):
    def test_serialise(self):
        cake = factories.CakeFactory()
        serialiser_data = serialisers.CakeSerialiser(cake).data
        self.assertEqual(serialiser_data["name"], cake.name)
        self.assertEqual(serialiser_data["comment"], cake.comment)
        self.assertEqual(serialiser_data["yumFactor"], cake.yum_factor)
        self.assertEqual(serialiser_data["imageUrl"], cake.image_url)

    def test_deserialise(self):
        cake_data = {
            "name": "Chocolate Cake",
            "comment": "Yummy",
            "yumFactor": 5,
            "imageUrl": "https://www.google.com",
        }
        serialiser = serialisers.CakeSerialiser(data=cake_data)
        self.assertTrue(serialiser.is_valid(), serialiser.errors)
        cake = serialiser.save()
        self.assertEqual(cake.name, cake_data["name"])
        self.assertEqual(cake.comment, cake_data["comment"])
        self.assertEqual(cake.yum_factor, cake_data["yumFactor"])
        self.assertEqual(cake.image_url, cake_data["imageUrl"])

    def test_deserialise_invalid_yum_factor_high(self):
        cake_data = {
            "name": "Chocolate Cake",
            "comment": "Yummy",
            "yumFactor": 6,
            "imageUrl": "https://www.google.com",
        }
        serialiser = serialisers.CakeSerialiser(data=cake_data)
        self.assertFalse(serialiser.is_valid())
        self.assertEqual(
            serialiser.errors,
            {
                "yumFactor": [
                    ErrorDetail(
                        string="YumFactor must be between 1 and 5", code="invalid"
                    )
                ]
            },
        )

    def test_deserialise_invalid_yum_factor_low(self):
        cake_data = {
            "name": "Chocolate Cake",
            "comment": "Yummy",
            "yumFactor": -3,
            "imageUrl": "https://www.google.com",
        }
        serialiser = serialisers.CakeSerialiser(data=cake_data)
        self.assertFalse(serialiser.is_valid())
        self.assertEqual(
            serialiser.errors,
            {
                "yumFactor": [
                    ErrorDetail(
                        string="YumFactor must be between 1 and 5", code="invalid"
                    )
                ]
            },
        )
