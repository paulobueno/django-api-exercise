from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, ListingViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'listing', ListingViewSet)
router.register(r'booking', BookingViewSet)

urlpatterns = router.urls
