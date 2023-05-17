from django.urls import path
from . import views
from .views import AddPostView




urlpatterns = [
    path('', views.main, name='main'),
    # path('blog/', views.blog, name='main'),
    path("homeblog", views.homeBlog, name="home"),
    # path("blogs", views.blogs, name = "blogs"),
    path('blogs', AddPostView.as_view(),name='blogs'),
    # path("blogs/<int:id>", views.blogdetails, name = "blogdetails"),
]




