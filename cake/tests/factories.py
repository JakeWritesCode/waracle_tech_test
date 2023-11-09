from factory import Faker
from factory.django import DjangoModelFactory
from cake import models


class CakeFactory(DjangoModelFactory):
    class Meta:
        model = models.Cake

    name = Faker("name")
    comment = Faker("sentence")
    yum_factor = Faker("random_int", min=1, max=5)
    image_url = Faker("image_url")
