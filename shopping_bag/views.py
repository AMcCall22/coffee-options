from django.shortcuts import render, redirect

# Create your views here.


def view_shopping_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_shopping_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    sizes = None
    if 'bag_size' in request.POST:
        sizes = request.POST['bag_size']
    shopping_bag = request.session.get('shopping_bag', {})

    if sizes:
        if item_id in list(shopping_bag.keys()):
            if sizes in shopping_bag[item_id]['items_by_size'].keys():
                shopping_bag[item_id]['items_by_size'][sizes] += quantity
            else:
                shopping_bag[item_id]['items_by_size'][sizes] = quantity
        else:
            shopping_bag[item_id] = {'items_by_size': {sizes: quantity}}
    else:
        if item_id in list(shopping_bag.keys()):
            shopping_bag[item_id] += quantity
        else:
            shopping_bag[item_id] = quantity

    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)
