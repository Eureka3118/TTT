from django.shortcuts import render
from .models import Place, Category

def place_list(request):
    # Get category filter from URL parameters
    category_id = request.GET.get('category')
    categories = Category.objects.all()
    selected_category = None

    if category_id:
        # If category is selected, filter places by category
        selected_category = Category.objects.get(id=category_id)
        places = Place.objects.filter(category=category_id)
    else:
        # If no category selected, places will be empty
        places = []

    context = {
        'places': places,
        'categories': categories,
        'selected_category': selected_category,
    }
    
    return render(request, 'destinations/place_list.html', context)


def place_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    places = category.places.all()
    return render(request, 'destinations/place_list.html', {'places': places, 'categories': Category.objects.all()})
