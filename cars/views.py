from rest_framework import generics
from .serializers import(
    CarDetailSerializer,
    CarListSerializer,
)

# check if user is owner of post, we can change data
from .permissions import IsOwnerOrReadOnly
from .models import Car


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
    # check if user is owner of post, we can change data
    permission_classes = (IsOwnerOrReadOnly, )


