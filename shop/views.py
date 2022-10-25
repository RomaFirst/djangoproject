from django.shortcuts import redirect, render
from .models import Product, Commande
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')

       #si item-name est different de vide et n´est pas null
    if item_name !='' and item_name is not None:

         #a ce niveau on filtre les resultat en fonction du title... similiaire au like n sql 
        product_object = Product.objects.filter(title__icontains=item_name)

      #gestion de la pagination .
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_object': product_object})

    #fonction permettant d afficher les detail

def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'shop/detail.html', {'product': product_object}) 

 #FONCTION CHACKOUT
def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode= request.POST.get('zipcode')
        com = Commande(items=items,total=total, nom=nom, email=email, address=address, ville=ville, pays=pays, zipcode=zipcode)
        com.save()

        #rediriger le chein sur la fenetre de confirmation
        return redirect('confirmation')


    return render(request, 'shop/checkout.html') 
    
#declaration de  la fonction de confirmation de commande
def confimation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
    return render(request, 'shop/confirmation.html', {'name': nom})          