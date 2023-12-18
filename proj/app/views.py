from django.shortcuts import render, redirect
from .models import Products
from .forms import *


def index(request):
    products = Products.objects.all()
    return render(request, 'app/index.html', context={'products': products})


def create(request):
    if request.method == 'POST':

        form = AddProduct(request.POST)
        if form.is_valid():

            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            pic = form.cleaned_data['pic']


            Products.objects.create(title=title, content=content, pic=pic)
            return redirect('home')
        else:
            form = AddProduct()
            return render(request, 'app/create.html', context={'form': form})
    else:
        form = AddProduct()
        return render(request, 'app/create.html', context={'form': form})


def delete(request, id):
    try:
        products = Products.objects.get(id=id)
        products.delete()
        return redirect('home')
    except:
        return redirect('home')


def product(request, id):
    try:
        product = Products.objects.get(id=id)
        return render(request, 'app/product.html', context={'product': product})
    except:
        return redirect('home')


def update(request, id):
    try:
        products = Products.objects.get(id=id)
        if request.method == 'POST':
            products.title = request.POST.get('title')
            products.content = request.POST.get('content')
            products.pic = request.POST.get('pic')

            products.save()
            return redirect('home')
        else:
            return render(request, 'app/update.html', context={'products': products})
    except:
        return redirect('create')


