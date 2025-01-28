from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('profile/<str:mobile_number>/', views.profile_view, name='profile'),
    path('profile/<str:mobile_number>/update/', views.update_profile_view, name='update_profile'),
]
