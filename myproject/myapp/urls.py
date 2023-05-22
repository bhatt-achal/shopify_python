from django.urls import path,include
from .views import *;

urlpatterns = [
  path('',product_list,name="product_list"),
  path('generate_description/', generate_description, name='generate_description'),

]