from django.http import HttpResponseServerError
from django.shortcuts import render, redirect

from .models import Post
from .forms import PostForm, UpdatePostForm
from bs4 import BeautifulSoup
import requests
from django.shortcuts import get_object_or_404
from django.contrib import messages


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'post/home.html', context)


def create(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            website = requests.get(form.data['url'])
            sourcecode = BeautifulSoup(website.text, 'html.parser')
            find_image = sourcecode.select(
                'meta[content^="https://live.staticflickr.com/"]')
            try:
                image = find_image[0]['content']
            except:
                return HttpResponseServerError("No image found on the webpage.")

            post.image = image

            find_title = sourcecode.select('h1.photo-title')
            title = find_title[0].text.strip()
            post.title = title

            find_artist = sourcecode.select('a.owner-name')
            artist = find_artist[0].text.strip()
            post.artist = artist

            post.author = request.user

            post.save()
            form.save_m2m()
            return redirect('home')

    return render(request, 'post/create.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    context = {'post': post}
    return render(request, 'post/post_detail.html', context)


def update_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    form = UpdatePostForm(instance=post)
    if request.method == 'POST':
        form = UpdatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully')
            return redirect('home')
        else:
            messages.error(request, 'updated failed')
            return redirect('home')
    context = {'post': post, 'form': form}
    return render(request, 'post/update.html', context)


def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully')
        return redirect('home')
    return render(request, 'post/delete.html', {'post': post})
