from .models import Post
from django.shortcuts import render
# Syötteen katselu
def feed(request):
    posts = Post.objects.all().order_by('-created')
    return render(request, 'feed.html', {'posts': posts})