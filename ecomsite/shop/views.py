from django.shortcuts import render
from .models import Products
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