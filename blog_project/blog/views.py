from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from django.template import loader
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def main(request):
    trendingPosts = Post.objects.values('title', 'slug').annotate(
        likecount=Count('likes')).order_by('-likecount')[:3]
    posts = Post.objects.all()
    template = loader.get_template('main.html')

    page_num = request.GET.get('page', 1)
    paginator = Paginator(posts , 3) 
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
        'trendingPosts': trendingPosts,
    }
    return HttpResponse(template.render(context, request))


def blog(request):
    template = loader.get_template('blog_page.html')
    return HttpResponse(template.render())
