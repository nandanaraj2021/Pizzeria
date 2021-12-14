from django.shortcuts import render, redirect
# from .forms import ToppingForm
from .models import Pizza

# Create your views here.
def index(request):
    return render(request, "pizzas/index.html")

def pizzas(request):
    pizzas = Pizza.objects.order_by('name')

    context = {'pizzas':pizzas}

    return render(request, "pizzas/pizzas.html", context)


def toppings(request, pizza_id):
    t = Pizza.objects.get(id=pizza_id)
    
    toppings = t.topping_set.all()

    context = {'pizzas':pizzas,'toppings':toppings}

    return render(request, "pizzas/toppings.html", context)

# def comments(request, pizza_id):
#     t = Pizza.objects.get(id=pizza_id)
#     if request.method != 'POST':
#         form = ToppingForm()
#     else:
#         form = ToppingForm(data=request.POST)

#         if form.is_valid():
#             comments = form.save(commit=False)
#             comments.t = t
#             comments.save()
#             return redirect('pizzas:toppings',pizza_id=pizza_id)

#     context = {'form':form, 'pizzas':pizzas}
#     return render(request, 'pizzas/comments.html', context)