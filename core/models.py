from djongo import models


class PizzaSize(models.Model):

    name = models.CharField(max_length=255)
    objects = models.DjongoManager()

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
    objects = models.DjongoManager()

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
    )
    type_pizza = models.CharField(
        max_length=20,
        choices=PIZZA_TYPE,
        default='regular',
        verbose_name='Type Of Pizza'
    )
    size_pizza = models.CharField(
        max_length=120,
        verbose_name='Size Of Pizza',
        blank=False,
        null=False
    )
    topping_pizza = models.CharField(
        max_length=120,
        verbose_name='Topping For Pizza',
        blank=False,
        null=False
    )
    description = models.TextField(blank=True, null=True)

    objects = models.DjongoManager()

    class Meta:
        verbose_name = "Pizza"
        verbose_name_plural = "Pizzas"

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        return super(Pizza, self).save(*args, **kwargs)
