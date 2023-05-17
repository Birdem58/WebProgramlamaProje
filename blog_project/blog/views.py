from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from django.template import loader
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView


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



kategori_liste = ["teknoloji","tarih","bilimkurgu","uzay"]
# baslik_liste = [
#     {
#         "id": 1,
#         "baslik_adi":"blog 1",
#         "aciklama":"blog 1 aciklama",
#         "resim": "b1.jpg",
#         "anasayfa":True,
#     },
#     {
#         "id": 2,
#         "baslik_adi":"blog 2",
#         "aciklama":"blog 2 aciklama",
#         "resim": "b2.jpg",
#         "anasayfa":True,
#     },
#     {
#         "id": 3,
#         "baslik_adi":"blog 3",
#         "aciklama":"blog 3 aciklama",
#         "resim": "b3.jpg",
#         "anasayfa":False,
#     },
#     {
#         "id": 4,
#         "baslik_adi":"blog 4",
#         "aciklama":"blog 4 aciklama",
#         "resim": "b4.jpg",
#         "anasayfa":False,
#     },
    
    
#     ]

def blog(request):
    template = loader.get_template('blog_page.html')
    return HttpResponse(template.render())


def homeBlog(request):
    data = {
        "kategoriler":kategori_liste,
        "basliklar":Post.objects.all(),
    }
    return render(request, "blog.html",data)


def blogs(request):
    
        
    data = {
        
        "basliklar":Post.objects.all(),
    }
    return render(request,"blogs.html",data)



# def blogdetails(request,id):
#     data = {
#         "id":id
#     }
#     return render(request,"blogdetails.html",data)


class AddPostView(CreateView):
    model = Post
    template_name = "blogs.html"
    fields = '__all__'

