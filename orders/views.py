from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from . models import Confirm, Orders, Pizza, Pastas, RegularPizza, SicilianPizza, Subs, Extras, Toppings, Salads, DinnerPlatters

# Create your views here.


def pizza(request):
    if request.user.is_authenticated:
        regular_pizza = RegularPizza.objects.all()
        sicilian_pizza = SicilianPizza.objects.all()
        toppings = Toppings.objects.all()
        context = {
            'regular_pizza': regular_pizza,
            'sicilian_pizza': sicilian_pizza,
            'toppings': toppings
        }
        return render(request, 'orders/pizza.html', context)
    elif request.user.is_anonymous:
        return HttpResponseRedirect(reverse('login'))


def pasta(request):
    if request.user.is_authenticated:
        pastas = Pastas.objects.all()
        context = {
            'pastas': pastas
        }
        return render(request, 'orders/pasta.html', context)
    elif request.user.is_anonymous:
        return HttpResponseRedirect(reverse('login'))


def subs(request):
    if request.user.is_authenticated:
        subs = Subs.objects.all()
        extras = Extras.objects.all()
        context = {
            'subs': subs,
            'extras': extras
        }
        return render(request, 'orders/subs.html', context)
    elif request.user.is_anonymous:
        return HttpResponseRedirect(reverse('login'))


def salads(request):
    if request.user.is_authenticated:
        salads = Salads.objects.all()
        context = {
            'salads': salads
        }
        return render(request, 'orders/salad.html', context)
    elif request.user.is_anonymous:
        return HttpResponseRedirect(reverse('login'))


def dinner_platters(request):
    if request.user.is_authenticated:
        dinner_platters = DinnerPlatters.objects.all()
        context = {
            'dinner_platters': dinner_platters
        }
        return render(request, 'orders/dinnerplatters.html', context)
    elif request.user.is_anonymous:
        return HttpResponseRedirect(reverse('login'))


def added(request):
    dish = request.POST['dish']
    type = request.POST['type']
    size = request.POST['size']
    price = request.POST['price']

    try:
        addition1 = request.POST["checkbox0"]
    except KeyError:
        addition1 = None
    try:
        addition2 = request.POST["checkbox1"]
    except KeyError:
        addition2 = None
    try:
        addition3 = request.POST["checkbox2"]
    except KeyError:
        addition3 = None
    try:
        addition4 = request.POST["checkbox3"]
    except KeyError:
        addition4 = None
    try:
        addition5 = request.POST["checkbox4"]
    except KeyError:
        addition5 = None
    try:
        extra_cheese = request.POST["extra_cheese"]
    except KeyError:
        extra_cheese = None
    try:
        topping1 = request.POST["toppings0"]
    except KeyError:
        topping1 = None
    try:
        topping2 = request.POST["toppings1"]
    except KeyError:
        topping2 = None
    try:
        topping3 = request.POST["toppings2"]
    except KeyError:
        topping3 = None
    try:
        topping4 = request.POST["toppings3"]
    except KeyError:
        topping4 = None
    try:
        topping5 = request.POST["toppings4"]
    except KeyError:
        topping5 = None

    if topping1:
        topping_to_add1 = Toppings.objects.get(id=topping1)
    if topping2:
        topping_to_add2 = Toppings.objects.get(id=topping2)
    if topping3:
        topping_to_add3 = Toppings.objects.get(id=topping3)
    if topping4:
        topping_to_add4 = Toppings.objects.get(id=topping4)
    if topping5:
        topping_to_add5 = Toppings.objects.get(id=topping5)
    if extra_cheese:
        cheese_to_add = Extras.objects.filter(extra='Extra Cheese')
    if addition1:
        addition_to_add1 = Extras.objects.filter(extra=addition1)
    if addition2:
        addition_to_add2 = Extras.objects.filter(extra=addition2)
    if addition3:
        addition_to_add3 = Extras.objects.filter(extra=addition3)
    if addition4:
        addition_to_add4 = Extras.objects.filter(extra=addition4)
    if addition5:
        addition_to_add5 = Extras.objects.filter(extra=addition5)
    order = Orders(dish=dish, pizza_type=type, size=size, price=price,
                   username=request.user.username, order_status=False)
    order.save()
    if topping1:
        order.pizza_toppings.add(topping_to_add1)
    if topping2:
        order.pizza_toppings.add(topping_to_add2)
    if topping3:
        order.pizza_toppings.add(topping_to_add3)
    if topping4:
        order.pizza_toppings.add(topping_to_add4)
    if topping5:
        order.pizza_toppings.add(topping_to_add5)
    if extra_cheese:
        order.sub_additions.add(cheese_to_add[0])
    if addition1:
        order.sub_additions.add(addition_to_add1[0])
    if addition2:
        order.sub_additions.add(addition_to_add2[0])
    if addition3:
        order.sub_additions.add(addition_to_add3[0])
    if addition4:
        order.sub_additions.add(addition_to_add4[0])
    if addition5:
        order.sub_additions.add(addition_to_add5[0])

    order.save()
    request.session['cart'] = True
    return JsonResponse({"success": True})


def cart(request):
    orders = Orders.objects.filter(username=request.user.username)
    context = {
        'orders': orders
    }
    return render(request, "orders/cart.html", context)


def delete(request):
    id = request.POST['id']
    try:
        no_content = request.POST["no_content"]
    except KeyError:
        no_content = None

    order = Orders.objects.get(id=id)

    order.delete()
    if no_content == 'no_content':
        request.session["cart"] = False

    return JsonResponse({"success": True})


def place_order(request):
    confirm_orders = Orders.objects.filter(username=request.user.username)
    for order in confirm_orders:
        confirmation = Confirm(dish=order.dish, pizza_type=order.pizza_type,
                               size=order.size, price=order.price, username=order.username, order_status=False)
        confirmation.save()
        confirmation.pizza_toppings.set(order.pizza_toppings.all())
        confirmation.sub_additions.set(order.sub_additions.all())
        confirmation.save()
        order.delete()
    return HttpResponseRedirect(reverse('pizza'))


def confirm_order(request):
    orders = Confirm.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'orders/confirm.html', context)
