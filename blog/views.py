from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    post = Post.object.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'bolg/post_detail.html', {'post': post})