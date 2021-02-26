from django.urls import path
from cars.views import CarCreateView

app_name = 'cars'

urlpatterns = [
    path('create/', CarCreateView.as_view()),
]