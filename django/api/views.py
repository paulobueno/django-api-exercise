from rest_framework import viewsets
from .models import Property
from .serializers import PropertySerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def list(self, request, *args, **kwargs):
        property_code = self.request.query_params.get('property_code', None)

        if property_code:
            self.queryset = Property.objects.filter(property_code=property_code)
        return super().list(request, *args, **kwargs)
