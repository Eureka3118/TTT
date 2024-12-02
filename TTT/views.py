from django.shortcuts import render, get_object_or_404 
from blog.models import Post
from gallery.models import Gallery  
from destinations.models import Place, Category

def travel_recommendations(request):
    return render(request, 'TTT/recommendations.html')



def home(request):
    categories = Category.objects.all()
    latest_posts = Post.objects.order_by('-created_at')[:3]  
    latest_places = Place.objects.order_by('-created_at')[:3]  
    latest_galleries = Gallery.objects.order_by('-created_at')[:3]
    admin_galleries = Gallery.objects.all().order_by('-created_at')[:6]

    context = {
        'latest_posts': latest_posts,
        'latest_places': latest_places,
        'latest_galleries': latest_galleries,
        'admin_galleries': admin_galleries,
        'categories': categories,
}
    return render(request, 'TTT/home.html', context)

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    places = Place.objects.filter(category=category)
    context = {
        'category': category,
        'places': places,
    }
    return render(request, 'TTT/category_detail.html', context)

def places_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    places = Place.objects.filter(category=category)
    context = {
        'category': category,
        'places': places,
    }
    return render(request, 'TTT/places_by_category.html', context)

def place_list(request):
    category_id = request.GET.get('category')
    if category_id:
        places = Place.objects.filter(category_id=category_id)
        category = Category.objects.get(id=category_id)
    else:
        places = Place.objects.all()
        category = None

    context = {
        'places': places,
        'category': category,
    }
    return render(request, 'TTT/place_list.html', context)
