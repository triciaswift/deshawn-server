from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from deshawnapi.views import WalkerView, CityView, DogView, AppointmentView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"walkers", WalkerView, "walk")
router.register(r"cities", CityView, "city")
router.register(r"dogs", DogView, "dog")
router.register(r"appointments", AppointmentView, "appointment")

# First argument = what you want URL path to be
# Second argument = view that will handle client requests to that route
# Third argument = needed in order for a route to be registered

urlpatterns = [
    path("", include(router.urls)),
]
