from django.shortcuts import render

from .models import Pizza

# Create your views here.
def index(request):
    return render(request, "pizzas/index.html")

def pizzas(request):
    pizzas = Pizza.objects.order_by('name')

    context = {'pizzas':pizzas}

    return render(request, "pizzas/pizzas.html", context)


def toppings(request, pizza_id):
    topic = Pizza.objects.get(id=pizza_id)
    
    context = {'toppings':toppings}

    return render(request, "pizzas/toppings.html", context)
