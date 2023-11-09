from rest_framework import serializers
from cake import models


class CakeSerialiser(serializers.ModelSerializer):
    imageUrl = serializers.CharField(source="image_url")
    yumFactor = serializers.IntegerField(source="yum_factor")

    class Meta:
        model = models.Cake
        fields = ["id", "name", "comment", "imageUrl", "yumFactor"]

    def validate_yumFactor(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("YumFactor must be between 1 and 5")
        return value
