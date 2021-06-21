from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('type_pizza', 'size_pizza')

    def create(self, *args, **kwargs):
        try:
            return super(ListCreatePizzaView, self).create(*args, **kwargs)
        except PizzaSize.DoesNotExist:
            return Response({'message': 'This size of pizza dosn\'t exist in menu.'}, status=HTTP_404_NOT_FOUND)
        except PizzaTopping.DoesNotExist:
            return Response({'message': 'This type of topping on pizza dosn\'t exist in menu.'}, status=HTTP_404_NOT_FOUND)


class EditDeletePizzaView(RetrieveUpdateDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
