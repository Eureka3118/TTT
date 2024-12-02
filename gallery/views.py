from django.shortcuts import render, get_object_or_404, redirect
from .models import Gallery, Image, Rating  # Add Rating to imports
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Avg  # Add this import
import json  # Add this import
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from .forms import GalleryForm  # You'll need to create this form

@login_required
def gallery_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        cover_image = request.FILES.get('cover_image')  

        gallery = Gallery.objects.create(
            user=request.user,
            title=title,
            description=description,
            cover_image=cover_image
        )
        
        images = request.FILES.getlist('images')
        for image in images:
            Image.objects.create(gallery=gallery, image=image)
        
        return redirect('gallery:gallery_list')

    return render(request, 'gallery/gallery_form.html')

@login_required
def gallery_detail(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)
    return render(request, 'gallery/gallery_detail.html', {'gallery': gallery})

@login_required
def upload_gallery_image(request, gallery_id):
    if request.method == 'POST':
        gallery = get_object_or_404(Gallery, id=gallery_id)
        images = request.FILES.getlist('images') 

        for img in images:
            Image.objects.create(gallery=gallery, image=img)

        return redirect('gallery:gallery_detail', pk=gallery.id)

    return render(request, 'gallery/upload_image.html')

def gallery_list(request):
    galleries = Gallery.objects.all().order_by('-created_at')
    paginator = Paginator(galleries, 12)  # Show 12 galleries per page
    
    page = request.GET.get('page')
    galleries = paginator.get_page(page)
    
    context = {
        'galleries': galleries,
        'is_paginated': paginator.num_pages > 1,
        'page_obj': galleries,
    }
    return render(request, 'gallery/gallery_list.html', context)

@login_required  # Add this decorator
def rate_gallery(request, gallery_id):  # Fix indentation here
    if request.method == 'POST':
        data = json.loads(request.body)
        rating = data.get('rating')
        gallery = get_object_or_404(Gallery, id=gallery_id)  # Use get_object_or_404
        
        # Create or update rating
        rating_obj, created = Rating.objects.update_or_create(
            user=request.user,
            gallery=gallery,
            defaults={'value': rating}
        )
        
        # Calculate new average
        avg_rating = gallery.ratings.aggregate(Avg('value'))['value__avg']
        count = gallery.ratings.count()
        
        return JsonResponse({
            'rating': avg_rating,
            'count': count
        })
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)  # Add error handling

@login_required
@require_POST
def rate_gallery(request, gallery_id):
    try:
        gallery = Gallery.objects.get(id=gallery_id)
        rating_value = int(request.POST.get('rating'))
        
        rating, created = Rating.objects.update_or_create(
            user=request.user,
            gallery=gallery,
            defaults={'value': rating_value}
        )
        
        # Recalculate average rating
        average_rating = Rating.objects.filter(gallery=gallery).aggregate(Avg('value'))['value__avg']
        gallery.average_rating = average_rating
        gallery.save()
        
        return JsonResponse({
            'status': 'success',
            'rating': average_rating,
            'count': gallery.ratings.count()
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'userapp/profile.html', {'profile_user': user})

@login_required
def gallery_edit(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)
    
    # Check if the user is the owner of the gallery
    if request.user != gallery.user:
        return redirect('gallery:gallery_detail', pk=pk)
    
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=gallery)
        if form.is_valid():
            form.save()
            return redirect('gallery:gallery_detail', pk=pk)
    else:
        form = GalleryForm(instance=gallery)
    
    return render(request, 'gallery/gallery_edit.html', {
        'form': form,
        'gallery': gallery
    })