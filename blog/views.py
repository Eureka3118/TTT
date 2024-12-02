from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

import re
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from destinations.models import Category
from django.template.loader import render_to_string
import logging

logger = logging.getLogger(__name__)

def post_list(request):
    sort_by = request.GET.get('sort', 'recent')  # Default to 'recent'
    
    if sort_by == 'oldest':
        posts = Post.objects.all().order_by('created_at')
    else:  # Default to 'recent'
        posts = Post.objects.all().order_by('-created_at')
    
    context = {
        'posts': posts,
        'sort_by': sort_by,
    }
    return render(request, 'blog/post_list.html', context) 



@csrf_exempt
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    
    context = {
        'post': post,
        'comments': comments,
    }
    return render(request, 'blog/post_detail.html', context)

def search_posts(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.all()
    return render(request, 'blog/search_results.html', {'posts': posts})

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'blog/profile.html', {
        'profile_user': user,
    })

def destination_categories(request):
    return {
        'destination_categories': Category.objects.all()
    }

@login_required
def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        is_published = request.POST.get('is_published') == 'on'
        
        post = Post.objects.create(
            title=title,
            content=content,
            image=image,
            author=request.user,
            is_published=is_published
        )
        
        return redirect('blog:post_detail', pk=post.pk)
    
    return render(request, 'blog/post_form.html')

@login_required
def add_comment(request, post_id):
    if request.method == 'POST':
        try:
            post = get_object_or_404(Post, id=post_id)
            content = request.POST.get('content', '').strip()
            
            if not content:
                return HttpResponseBadRequest('Comment content is required')
            
            # Create the comment
            comment = Comment.objects.create(
                post=post,
                author=request.user,
                content=content
            )
            
            # For AJAX requests, return the comment HTML
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                html = render_to_string(
                    'blog/comment.html',
                    {'comment': comment},
                    request=request
                )
                return HttpResponse(html)
            
            # For regular requests, redirect back to the post
            return redirect('blog:post_detail', pk=post.id)
            
        except Exception as e:
            print(f"Error adding comment: {str(e)}")  # For debugging
            return HttpResponseBadRequest(str(e))
    
    return HttpResponseBadRequest('Only POST requests are allowed')

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if request.user == comment.author:
        comment.delete()
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return HttpResponse(status=204)
    
    return redirect('blog:post_detail', pk=comment.post.id)

def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        print(f"Deleting post: {post.title}")  
        post.delete()
        return redirect(reverse('blog:post_list'))  
    return redirect(reverse('blog:post_detail', args=[post_id]))