from django.urls import path, include
from core.views import PizzaSizeView, PizzaToppingView,  ListCreatePizzaView

app_name = "core"

urlpatterns = [
    path('pizza-size/', PizzaSizeView.as_view()),
    path('pizza-topping/', PizzaToppingView.as_view()),
    path('pizza/', ListCreatePizzaView.as_view()),
]