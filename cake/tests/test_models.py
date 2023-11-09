from django.db import DataError
from django.test import TestCase
from cake import models


class TestCake(TestCase):
    def test_cake_str(self):
        cake = models.Cake(name="Chocolate Cake")
        self.assertEqual(str(cake), "Chocolate Cake")

    def test_save(self):
        cake = models.Cake(
            name="Chocolate Cake",
            comment="t",
            image_url="https://www.google.com",
            yum_factor=5,
        )
        cake.save()
        self.assertEqual(cake.name, "Chocolate Cake")
        self.assertEqual(cake.comment, "t")
        self.assertEqual(cake.image_url, "https://www.google.com")
        self.assertEqual(cake.yum_factor, 5)

    def test_cake_name_max_length(self):
        cake = models.Cake(
            name="a" * 30, comment="t", image_url="https://www.google.com", yum_factor=5
        )
        cake.save()
        self.assertEqual(cake.name, "a" * 30)

        with self.assertRaises(DataError):
            cake.name = "a" * 31
            cake.save()

    def test_cake_comment_max_length(self):
        cake = models.Cake(
            name="Chocolate Cake",
            comment="a" * 200,
            image_url="https://www.google.com",
            yum_factor=5,
        )
        cake.save()
        self.assertEqual(cake.comment, "a" * 200)

        with self.assertRaises(DataError):
            cake.comment = "a" * 201
            cake.save()
