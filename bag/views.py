from django.shortcuts import render


def view_bag(request):
    """ Shows bag contents page """

    return render(request, 'bag/bag.html')
