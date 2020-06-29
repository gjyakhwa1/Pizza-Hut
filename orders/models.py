from django.db import models

# Create your models here.


class Pizza(models.Model):
    pizza = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.pizza}'


class Toppings(models.Model):
    topping = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.topping}'


class RegularPizza(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="regular_pizza")
    price_small = models.DecimalField(max_digits=5, decimal_places=2)
    price_large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'Regular:{self.pizza}--small:{self.price_small}--large{self.price_large}'


class SicilianPizza(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="sicilian_pizza")
    price_small = models.DecimalField(max_digits=5, decimal_places=2)
    price_large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'Sicilian:{self.pizza}--small:{self.price_small}--large{self.price_large}'


class Extras(models.Model):
    extra = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.extra}'


class Subs(models.Model):
    sub = models.CharField(max_length=30)
    small_price = models.DecimalField(max_digits=5, decimal_places=2)
    large_price = models.DecimalField(max_digits=5, decimal_places=2)
    extra = models.ManyToManyField(Extras, blank=True, related_name="subs")

    def __str__(self):
        return f'Sub:{self.sub}--small:{self.small_price}--large{self.large_price}'


class Pastas(models.Model):
    pasta = models.CharField(max_length=35)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.pasta}--price:{self.price}'


class Salads(models.Model):
    salad = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.salad}--price:{self.price}'


class DinnerPlatters(models.Model):
    dinner_platters = models.CharField(max_length=30)
    small_price = models.DecimalField(max_digits=5, decimal_places=2)
    large_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.dinner_platters}--small:{self.small_price}--large:{self.large_price}'


class Orders(models.Model):
    dish = models.CharField(max_length=40)
    pizza_type = models.CharField(max_length=40, null=True, blank=True)
    size = models.CharField(max_length=15, null=True, blank=True)
    pizza_toppings = models.ManyToManyField(Toppings, related_name="orders", blank=True)
    sub_additions = models.ManyToManyField(Extras, related_name="orders", blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    username = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now=True)
    order_status = models.BooleanField(default=False)

    def convert_to_tuple(self, query, object):
        list = query
        output = []
        if object == 'topping':
            for elem in list:
                output.append(elem.topping)
        else:
            for elem in list:
                output.append(elem.extra)
        return tuple(output)

    def __str__(self):
        return f"{self.id} | {self.dish} Type: {self.pizza_type} Size: {self.size} Toppings: {self.convert_to_tuple(self.pizza_toppings.all(), 'topping')} Extras: {self.convert_to_tuple(self.sub_additions.all(), 'extra')} Price: {self.price} For: {self.username} At: {self.time.hour}:{self.time.minute}-{self.time.day}/{self.time.month}/{self.time.year} Status: {self.order_status}"


class Confirm(models.Model):
    dish = models.CharField(max_length=40)
    pizza_type = models.CharField(max_length=40, null=True, blank=True)
    size = models.CharField(max_length=15, null=True, blank=True)
    pizza_toppings = models.ManyToManyField(Toppings, related_name="confirmations", blank=True)
    sub_additions = models.ManyToManyField(Extras, related_name="confirmations", blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    username = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now=True)
    order_status = models.BooleanField(default=False)

    def convert_to_tuple(self, query, object):
        list = query
        output = []
        if object == 'topping':
            for elem in list:
                output.append(elem.topping)
        else:
            for elem in list:
                output.append(elem.extra)
        return tuple(output)

    def __str__(self):
        return f"{self.id} | {self.dish} Type: {self.pizza_type} Size: {self.size} Toppings: {self.convert_to_tuple(self.pizza_toppings.all(), 'topping')} Extras: {self.convert_to_tuple(self.sub_additions.all(), 'extra')} Price: {self.price} For: {self.username} At: {self.time.hour}:{self.time.minute}-{self.time.day}/{self.time.month}/{self.time.year} Status: {self.order_status}"
