from django.urls import path
from shop.views import index, detail, checkout, confimation

#creation des urls pour les differentes views
urlpatterns = [
    path('', index, name='home'),

      #url dynamique, le chemin change en fonction du id
    path('<int:myid>', detail, name="detail"),
    path('checkout', checkout, name="checkout"),
    path('confirmation', confimation, name="confirmation" ),
]

