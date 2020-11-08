from django.shortcuts import render

def view_shopping_bag(request):
    """A view to return the index page"""

    return render(request, 'shopping_bag/shopping_bag.html')