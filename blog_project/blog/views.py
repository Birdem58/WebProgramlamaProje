from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from django.template import loader
from .models import Post


def main(request):
    trendingPosts = Post.objects.values('title', 'slug').annotate(
        likecount=Count('likes')).order_by('-likecount')[:3]
    posts = Post.objects.all()
    template = loader.get_template('main.html')
    #print(posts[0].author)
    context = {
        'posts': posts,
        'trendingPosts': trendingPosts,
    }
    return HttpResponse(template.render(context, request))


def blog(request):
    return HttpResponse("blog")
