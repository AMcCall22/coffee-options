from django.shortcuts import get_object_or_404
from products.models import Bean


def shopping_bag_contents(request):

    shopping_bag_items = []
    total = 0
    bean_count = 0
    shopping_bag = request.session.get('shopping_bag', {})

    for item_id, item_data in shopping_bag.items():
        if isinstance(item_data, int):
            bean = get_object_or_404(Bean, pk=item_id)
            total += item_data * bean.price
            bean_count += item_data
            shopping_bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'bean': bean,
            })

        else:
            bean = get_object_or_404(Bean, pk=item_id)
            for sizes, quantity in item_data['items_by_size'].items():
                total += quantity * bean.price
                bean_count += quantity
                shopping_bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'bean': bean,
                    'size': sizes,
                })

    grand_total = total

    context = {
        'shopping_bag_items': shopping_bag_items,
        'total': total,
        'bean_count': bean_count,
        'grand_total': grand_total,
    }

    return context
