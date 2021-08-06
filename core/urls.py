from django.urls import path, include
from core.views import (
    PizzaSizeView,
    PizzaToppingView,
    ListCreatePizzaView,
    EditDeletePizzaView,
)

app_name = "core"

urlpatterns = [
    path('pizza-size/', PizzaSizeView.as_view(), name='pizza_size'),
    path('pizza-topping/', PizzaToppingView.as_view(), name='pizza_topping'),
    path('pizza/', ListCreatePizzaView.as_view(), name='pizza'),
    path('pizza/<int:pk>', EditDeletePizzaView.as_view(), name='pizza_id'),
]
