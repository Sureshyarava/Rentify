from .models import Property

from rest_framework.serializers import ModelSerializer


class PropertySerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"

class CustomPropertySerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = ["image","area","place","number_of_bedrooms","number_of_bathrooms"]