from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

def home(request):
    return render(request,'tienda/home.html')

def administration(request):
    products = Product.objects.all()
    return render(request,'tienda/administration.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'tienda/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'tienda/product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('administration')
    else:
        form = ProductForm()
    return render(request, 'tienda/product_create.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect('administration')
    else:
        form = ProductForm(instance=product)
    return render(request, 'tienda/product_update.html', {'form': form, 'product': product})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('administration')
    return render(request, 'tienda/product_delete.html', {'product': product})


