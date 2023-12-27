from django.shortcuts import (render, get_object_or_404,
                              HttpResponseRedirect, redirect,
                              reverse, HttpResponse)
from django.http import HttpResponseServerError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import JsonResponse


from .models import WishList
from products.models import Product


@login_required
def wish_list(request):
    """
    view to render the wishlist page
    """
    poster_wishlist = WishList.objects.filter(user_id=request.user)
    template = 'wishlist/wishlist.html'
    context = {
        'poster_wishlist': poster_wishlist,
    }
    return render(request, template, context)


@login_required
def add_wish(request):
    """user can add a poster to their wishlist"""

    if request.method == 'POST':
        product_id = request.POST.get('product-id')
        product = get_object_or_404(Product, id=product_id)
        redirect_url = request.POST.get('my_redirect_url')
        try:
            wish_item = WishList.objects.get(user_id=request.user, product_id=product)
            if wish_item:
                messages.info(request, f'{wish_item.product} is already on your wishlist')
        except WishList.DoesNotExist:
            WishList.objects.create(user_id=request.user, product_id=product)
            messages.success(request, f'{product.name} poster has been added to your wishlist')

        return HttpResponseRedirect(redirect_url)

    return redirect('products')


@login_required
def delete_wish(request):
    """remove poster from wishlist"""
    if request.method == 'POST':
        item_id = request.POST.get('item-id')
        wish_item = get_object_or_404(WishList, pk=item_id, user_id=request.user)
        wish_item.delete()
        messages.success(request, f'{wish_item.product_id.name} has been deleted from your wishlist')
        return JsonResponse({'message': 'Item deleted successfully.'})
    return JsonResponse({'message': 'Invalid request.'}, status=400)