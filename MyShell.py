import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizzeria.settings')

import django
django.setup()

from pizzas.models import Pizza, Topping

pizzas = Pizza.objects.all()

for pizza in pizzas:
    print(pizza.id)
    print(pizza.name)

t = Pizza.objects.get(id=1)
print(t)

toppings = t.topping_set.all()

for e in toppings:
    print(e)