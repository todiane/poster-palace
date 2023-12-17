from django.shortcuts import render, redirect, reverse, get_object_or_404, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg, Count 
from django.db.models.functions import Lower
from .models import Product, Category, Review
from .forms import ReviewForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

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
    """ Shows individual product details and reviews """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def create_review(request, pk):
    """ Create a review for a product, takes request and product id """

    product = get_object_or_404(Product, pk=pk)
    user = request.user.userprofile
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = user
            review.save()
            messages.success(request, 'Your review has been added. Thank you!')
        else:
            messages.error(
                request, 'Review not added. Please fill in the form again.'
            )
    return redirect('product', pk)


@login_required
def delete_review(request, pk):
    """Handles deleting reviews, takes request and review id
    """
    review = get_object_or_404(Review, pk=pk)
    product = review.product

    if request.method == 'POST':
        user = request.user.userprofile
        if request.user.is_superuser or user == review.user:
            try:
                review.delete()
                messages.success(request, 'Review deleted successfully.')
            except ObjectDoesNotExist:
                messages.error(
                    request, 'Sorry. This review cannot be found.')
            return redirect('product', product.id)

    context = {
        'review': review,
        'product': product,
    }

    return render(request, 'reviews/delete_review.html', context)


@login_required
def edit_review(request, pk):
    """Handles editing reviews, takes request and review id
    """
    review = get_object_or_404(Review, pk=pk)
    product = review.product
    form = ReviewForm(instance=review)

    if request.method == 'POST':
        user = request.user.userprofile
        if request.user.is_superuser or user == review.user:
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                review = form.save()
                messages.success(request, 'Review updated successfully')
                return redirect('product', product.id)
            messages.error(
                request, 'Something went wrong. Please try again.')
        else:
            messages.error(
                request, 'You are not allowed to edit this review')

    context = {'review_form': form,
               'review': review,
               'product': product }
    return render(request, 'reviews/edit_review.html', context)