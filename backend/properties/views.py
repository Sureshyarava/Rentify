from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Property
from rest_framework.permissions import IsAuthenticated
from accounts.serializer import BasicUserSerializer
from accounts.models import CustomUser

from .serializers import CustomPropertySerializer, PropertySerializer


# Create your views here.

class PropertyView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        user_serializer = BasicUserSerializer(instance = request.user)
        data['user'] = user_serializer['id'].value
        serializer = PropertySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        if 'property_id' in kwargs:
            property = Property.objects.get(property_id = kwargs['property_id'])
            serializer = PropertySerializer(instance = property)
            user = serializer.data['user']
            user_instance = CustomUser.objects.get(id=user)
            user_serializer = BasicUserSerializer(instance = user_instance)
            combined_data = {
                    "user_details" : user_serializer.data,
                    "property_details" : serializer.data
                }
            return Response(data = combined_data, status=status.HTTP_200_OK)


class PropertyListView(APIView):
    def get(self, request):
        properties = list(Property.objects.all())
        serializer = CustomPropertySerializer(instance=properties, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)