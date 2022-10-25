
from django.contrib import admin
from .models import Category, Product,Commande

# Register your models here.
#personnalisation de l environrement django base
admin.site.site_header="E-Commerce"
admin.site.site_title="fashion-Shop"
admin.site.index_title="Manager"

class AdminCategorie(admin.ModelAdmin):
    list_display=('name', 'date_added')
    search_fields=('name',)


class AdminProduct(admin.ModelAdmin):
    list_display=('title', 'price', 'category', 'date_added')

    #afficher une barre de recherche 
    search_fields=('title',)
    list_editable=('price', )

class AdminCommande(admin.ModelAdmin):
    list_display=('items', 'nom', 'email', 'address', 'ville', 'pays','total', 'date_commande')
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategorie)
admin.site.register(Commande, AdminCommande)
search_fields=('nom',)
