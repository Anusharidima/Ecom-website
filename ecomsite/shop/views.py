from django.shortcuts import render
from .models import Products, Order
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    product_object = Products.objects.get_queryset().order_by('id')
    
    # search bar code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_object = product_object.filter(title__icontains=item_name)
        
    #Paginator code
    
    paginator = Paginator(product_object,3)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
     
    return render(request,'shop/index.html',context={'product_object':product_object})


def detail(request,id):
    product_objects = Products.objects.get(id=id)
    return render(request,'shop/detail.html',context={'product_objects':product_objects})

def checkout(request):
    
    if request.method == "POST":
        items = request.POST.get('items',"")
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        address2 = request.POST.get('address2',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")
        
        order = Order(items=items,name=name,email=email,address=address, address2=address2, city=city, state=state, zipcode=zipcode,total=total)
        order.save()    
    return render(request,'shop/checkout.html')