from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView
from django.core.paginator import Paginator


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        posts = Post.objects.filter(author_id=pk).order_by("-date_posted")
        p = Paginator(posts, 4)
        page_number = request.GET.get("page")
        page_obj = p.get_page(page_number)
        return render(request, 'users/profile.html', {'profile': profile, 'posts': posts, 'page_obj': page_obj})
    else:
        messages.success(request, 'You must sign in to view this page!')
        return redirect('login')


@login_required()
def profile_edit(request, pk):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated')
            return redirect('profile', pk)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile_edit.html', context)


class profile_delete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    success_url = '/'

    def test_func(self):
        profile = self.get_object()
        if self.request.user != profile.user:
            return True
        return False
