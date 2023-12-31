# basket_app.views.py
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from e_commerce_shop.basket_app.basket import Basket
from e_commerce_shop.products_app.models import Product


def basket_summary(request):
    basket = Basket(request)

    context = {
        'basket': basket,
    }
    return render(request, 'basket/summary.html', context)


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))  # -->> get product id
        product_qty = int(request.POST.get('productqty'))  # -->> get product qty
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, quantity=product_qty)
        basket_qty = basket.__len__()
        response = JsonResponse({
            'qty': basket_qty,
            'price': float(product.price),
        })

        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basket_qty = basket.__len__()
        basket_total = basket.get_total_price()
        response = JsonResponse({'qty': basket_qty, 'subtotal': float(basket_total)})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

        basket_qty = basket.__len__()
        basket_total = basket.get_total_price()
        response = JsonResponse({'qty': basket_qty, 'subtotal': float(basket_total)})
        return response
