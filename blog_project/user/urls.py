from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile-edit'),
    path("accounts/signup/", views.SignUpView.as_view(), name="signup"),
]