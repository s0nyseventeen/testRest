from django.urls import path
from cars.views import (
    CarCreateView,
    CarListView,
    CarDetailView,
)

app_name = 'cars'

urlpatterns = [
    path('create/', CarCreateView.as_view()),
    path('all/', CarListView.as_view()),
    path('car/detail/<int:pk>/', CarDetailView.as_view()),
]
