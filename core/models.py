from djongo import models


class PizzaSize(models.Model):

    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "PizzaSize"
        verbose_name_plural = "PizzaSizes"

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(PizzaSize, self).save(*args, **kwargs)


class PizzaTopping(models.Model):

    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "PizzaTopping"
        verbose_name_plural = "PizzaToppings"

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(PizzaTopping, self).save(*args, **kwargs)


class Pizza(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    PIZZA_TYPE = (
        ('regular', 'REGULAR'),
        ('square', 'SQUARE'),
        ('pie', 'PIE'),
    )
    type_pizza = models.CharField(
        max_length=20,
        choices=PIZZA_TYPE,
        default='regular',
        verbose_name='Type Of Pizza'
    )
    size_pizza = models.OneToOneField(
        PizzaSize,
        related_name='pizza',
        verbose_name='Size Of Pizza',
        on_delete=models.CASCADE
    )
    topping_pizza = models.OneToOneField(
        PizzaTopping,
        related_name='pizza',
        verbose_name='Topping For Pizza',
        on_delete=models.CASCADE
    )
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Pizza"
        verbose_name_plural = "Pizzas"

    def __str__(self):
        return str(self.name)
