from django.urls import path
from . import views


app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('restaurants/', views.restaurants, name='restaurants'),
    path('restaurants/<int:restaurant_id>', views.restaurant, name='restaurant'),
    path('restaurants/<int:restaurant_id>/food', views.food, name='food'),
    path('restaurants/<int:restaurant_id>/food/<int:dish_id>', views.dish, name='dish'),
    path('restaurants/<int:restaurant_id>/drinks', views.drinks, name='drinks'),
    path('restaurants/<int:restaurant_id>/drinks/<int:drink_id>', views.drink, name='drink'),

]
