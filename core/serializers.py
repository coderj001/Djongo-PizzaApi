from rest_framework.serializers import ModelSerializer

from core.models import (
    Pizza,
    PizzaSize,
    PizzaTopping
)


class PizzaSizeSerializer(ModelSerializer):

    class Meta:
        model = PizzaSize
        fields = ('name',)


class PizzaToppingSerializer(ModelSerializer):

    class Meta:
        model = PizzaTopping
        fields = ('name',)


class PizzaSerializer(ModelSerializer):

    class Meta:
        model = Pizza
        fields = (
            'id',
            'name',
            'type_pizza',
            'size_pizza',
            'topping_pizza',
            'description'
        )
        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        size_pizza = validated_data.pop('size_pizza')
        topping_pizza = validated_data.pop('topping_pizza')

        if size_pizza is not None:
            try:
                size_pizza_obj = PizzaSize.objects.get(name__iexact=size_pizza)
            except PizzaSize.DoesNotExist:
                raise e
        else:
            size_pizza_obj = PizzaSize.objects.first()

        if topping_pizza is not None:
            try:
                topping_pizza_obj = PizzaTopping.objects.get(
                    name__iexact=topping_pizza)
            except Exception as e:
                raise e
        else:
            topping_pizza_obj = PizzaTopping.objects.first()

        validated_data['size_pizza'] = size_pizza_obj.name
        validated_data['topping_pizza'] = topping_pizza_obj.name

        return super(PizzaSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        size_pizza = validated_data.pop('size_pizza')
        topping_pizza = validated_data.pop('topping_pizza')

        if size_pizza is not None:
            size_pizza_obj = PizzaSize.objects.get(name__iexact=size_pizza)
        else:
            size_pizza_obj = PizzaSize.objects.first()

        if topping_pizza is not None:
            topping_pizza_obj = PizzaTopping.objects.get(
                name__iexact=topping_pizza)
        else:
            topping_pizza_obj = PizzaTopping.objects.first()

        validated_data['size_pizza'] = size_pizza_obj.name
        validated_data['topping_pizza'] = topping_pizza_obj.name

        return super(PizzaSerializer, self).update(instance, validated_data)
