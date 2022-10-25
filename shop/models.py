import email
from email.headerregistry import Address
from enum import auto
from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

#creation de la table categoty, car chaque produit apparttienedra forceenet a une category de produit
class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
#La class Meta permet d afficher les nouvels enregistrements en premiere ligne a chaque mise a jours de la base
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name   

# Nous allons creer la table des produits et les classe par ordre d ajout

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE) 
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-date_added']

        def __str__(self):
            return self.title 

    #CLass commande

class Commande(models.Model):
        items = models.CharField(max_length=300)
        total = models.CharField(max_length=200)
        nom = models.CharField(max_length=150)
        email = models.EmailField()
        address = models.CharField(max_length=200)
        ville = models.CharField(max_length=200)
        pays = models.CharField(max_length=300)
        zipcode = models.CharField(max_length=300)
        date_commande = models.DateTimeField(auto_now= True)

        class Meta:
            ordering = ['-date_commande']

        def __str__(self):
            return self.nom

