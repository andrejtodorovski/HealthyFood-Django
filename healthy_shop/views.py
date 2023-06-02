from django.shortcuts import render

# Create your views here.
from .forms import ProductForm
from .models import Product, CustomUser


# Create your views here.

def index(request):
    return render(request, 'index.html')


def outofstock(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            product = form.save(commit=False)
            product.user = CustomUser.objects.all().filter(user=request.user).first()
            product.save()
    context = {
        "products": Product.objects.filter(quantity=0),
        "form": form
    }
    return render(request, 'outofstock.html', context=context)
