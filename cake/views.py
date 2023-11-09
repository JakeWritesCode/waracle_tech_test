from rest_framework import generics
from cake.models import Cake
from cake.serialisers import CakeSerialiser


"""
All cake data should come from the API, using standard GET/POST/DELETE HTTP
endpoints.

This is a little generic, but I'm taking this to mean that we need:
- A list view of all cakes
- A detail view of a single cake
- A create view for a new cake
- A delete view for an existing cake

No mention of a PATCH/PUT view, so I'm assuming that we don't need it.
"""


class CakesView(generics.ListCreateAPIView):
    """
    List all cakes, or create a new cake.
    """

    queryset = Cake.objects.all()
    serializer_class = CakeSerialiser


class CakeView(generics.RetrieveDestroyAPIView):
    """
    Retrieve or delete a cake instance.
    """

    queryset = Cake.objects.all()
    serializer_class = CakeSerialiser
