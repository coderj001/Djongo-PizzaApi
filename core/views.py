from rest_framework.generics import ListCreateAPIView

from core.models import (
    Pizza,
    PizzaSize,
    PizzaTopping
)

from core.serializers import (
    PizzaSerializer,
    PizzaSizeSerializer,
    PizzaToppingSerializer
)


class PizzaToppingView(ListCreateAPIView):
    queryset = PizzaTopping.objects.all()
    serializer_class = PizzaToppingSerializer


class PizzaSizeView(ListCreateAPIView):
    queryset = PizzaSize.objects.all()
    serializer_class = PizzaSizeSerializer


class ListCreatePizzaView(ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
