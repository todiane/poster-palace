from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.views.generic import TemplateView
from .models import Product, Category, Reviews
from .forms import ReviewForm


def all_products(request):
    """ Show all products, including sorting/search queries"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = "category__name"

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']

            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Shows individual product details and any reviews"""

    product = get_object_or_404(Product, pk=product_id)
    # Get any reviews that have been added
    reviews = Reviews.objects.filter(product_id=product_id, status=True)

    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(request, 'products/product_detail.html', context)



def submit_review(request, product_id):
    """ Logged in Users can leave a review"""
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = Reviews.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Your review has been updated.')
            
            return redirect(url)

        except Reviews.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = Reviews()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Your review has been submitted!')
                
                return redirect(url)

"""Compliance Pages for shipping, terms, privacy"""

class ShippingView(TemplateView):
    template_name = "compliance/shipping.html"

class PrivacyView(TemplateView):
    template_name = "compliance/privacy.html"

class TermsView(TemplateView):
    template_name = "compliance/terms.html"

class RefundView(TemplateView):
    template_name = "compliance/refund.html"
