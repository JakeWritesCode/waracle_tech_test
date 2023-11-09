from django.db import models


class Cake(models.Model):
    """Model representing a cake... tasty!"""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=200)
    # This could be a URL field to offer some additional validation,
    # but the spec states string, so no assumptions.
    image_url = models.TextField()
    yum_factor = models.IntegerField()

    def __str__(self):
        """String for representing the Model object."""
        return self.name
