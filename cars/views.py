from rest_framework import generics
from cars.serializers import(
    CarDetailSerializer,
    CarListSerializer,
)

from cars.models import Car


# create object
class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


# look up objects
class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()


# edit or delete object
class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()


