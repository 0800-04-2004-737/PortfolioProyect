from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.
def Post(request):
    posts = models.Post.objects.all()
    return render(request, "post.html", {"posts": posts})


def post_detail(request, post_id):
    post = get_object_or_404(models.Post, pk=post_id)
    return render(request, "post_detail.html", {"post": post})
