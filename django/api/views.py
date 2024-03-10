from rest_framework import viewsets
from .models import Property
from .serializers import PropertySerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = 'property_code'
    lookup_value_regex = '[A-Z]{4}\d{4}'
