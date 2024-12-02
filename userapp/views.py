from django.shortcuts import render, redirect, get_object_or_404 
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import PostForm, ProfileForm  
from .models import Profile
from blog.models import Post  
from django.core.exceptions import ObjectDoesNotExist
from gallery.models import Gallery
from django.contrib.auth import logout
from .models import Profile
from .forms import ProfileForm


def login_signup(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            # Login logic
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('TTT:home')  # Redirect to homepage on successful login
            else:
                messages.error(request, "Invalid credentials.")
        
        elif 'signup' in request.POST:
            # Signup logic
            username = request.POST.get('username')
            if User.objects.filter(username=username).exists():
                messages.warning(request, "This username is already used.")
            else:
                email = request.POST.get('email')
                password1 = request.POST.get('password1')
                password2 = request.POST.get('password2')
                if password1 == password2:
                    if len(password1) < 8:
                        messages.error(request, "Password must be at least 8 characters long.")
                    elif User.objects.filter(email=email).exists():
                        messages.warning(request, "This email is already associated with an account.")
                    else:
                        User.objects.create_user(username=username, email=email, password=password1)
                        messages.success(request, "Account created successfully! Please log in.")
                        return redirect('userapp:login_signup')  # Ensure correct namespace here
                else:
                    messages.error(request, "Passwords do not match.")
    
    return render(request, 'userapp/login_signup.html')



@login_required
def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=profile_user)
    user_galleries = Gallery.objects.filter(user=profile_user).order_by('-created_at')
    
    context = {
        'profile_user': profile_user,
        'galleries': user_galleries,
    }
    
    return render(request, 'userapp/profile_view.html', context)

@login_required
def edit_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile

    if request.method == 'POST':
        # Manually handle form data
        profile_image = request.FILES.get('profile_image')
        bio = request.POST.get('bio')
        location = request.POST.get('location')

        # Update profile fields
        if profile_image:
            profile.profile_image = profile_image
        profile.bio = bio
        profile.location = location

        # Save the profile
        profile.save()
        messages.success(request, 'Your profile has been updated successfully!')
        return redirect('userapp:profile', username=username)

    return render(request, 'userapp/edit_profile.html', {'profile': profile})

@login_required
def edit_post(request, post_id):
    profile = Profile.objects.get(user=request.user)
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully.")
            return redirect('blog:post_detail', pk=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect('blog:post_list')
    return render(request, 'blog/delete_post.html', {'post': post})

# def logout(request):
#     auth_logout(request)
#     messages.success(request, "You have successfully logged out.")
#     return redirect('TTT:home')

@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login_signup')  # or whatever your login page URL name is
    return render(request, 'userapp/logout.html')

@login_required
def logout_confirm(request):
    if request.method == 'POST':
        logout(request)
        return redirect('userapp:login_signup')
    else:  # GET request
        return render(request, 'userapp/logout.html')  # Make sure this template exists
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

