from django.contrib import admin
from . models import Pizza, Toppings, Pastas, Subs, RegularPizza, SicilianPizza, Extras, Salads, DinnerPlatters, Orders, Confirm
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ("pizza_toppings", "sub_additions")


admin.site.register(Pizza)
admin.site.register(Toppings)
admin.site.register(Pastas)
admin.site.register(Subs)
admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(Extras)
admin.site.register(Salads)
admin.site.register(DinnerPlatters)
admin.site.register(Orders, OrderAdmin)
admin.site.register(Confirm)
