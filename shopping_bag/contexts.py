from django.shortcuts import get_object_or_404
from products.models import Bean


def shopping_bag_contents(request):

    shopping_bag_items = []
    total = 0
    product_count = 0
    bean_count = 0
    shopping_bag = request.session.get('shopping_bag', {})

    for item_id, quantity in shopping_bag.items():
        bean = get_object_or_404(Bean, pk=item_id)
        total += quantity * bean.price
        bean_count += quantity
        shopping_bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'bean': bean,
        })

    grand_total = total

    context = {
        'shopping_bag_items': shopping_bag_items,
        'total': total,
        'product_count': product_count,
        'bean_count': bean_count,
        'grand_total': grand_total,
    }

    return context
