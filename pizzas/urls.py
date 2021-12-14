from django.urls import path

from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'pizzas'

urlpatterns = [
    path('', views.index, name='index'),
    path('pizzas', views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>/', views.toppings, name='toppings'),
    # path('comments/<int:pizza_id>/', views.comments, name='comments'),
]

urlpatterns += staticfiles_urlpatterns()