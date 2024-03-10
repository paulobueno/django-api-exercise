from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Property, Listing, Booking
from .serializers import PropertySerializer, ListingSerializer, BookingSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = 'property_code'
    lookup_value_regex = '[A-Z]{4}\d{4}'


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    lookup_field = 'id'
    lookup_value_regex = '\d+'

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    lookup_field = 'booking_code'
    lookup_value_regex = '[A-Z]{4}\d{4}'

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)