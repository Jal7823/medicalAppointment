from django.contrib import admin
from django.urls import path, include
from .views import LoginFromView,LogoutView,register_form,register,UserProfile,DetailUserProfile,createNumberMembership

urlpatterns = [
    path('', LoginFromView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('registro/',register_form, name='registro'),
    path('userProfile/<int:pk>',UserProfile.as_view(), name='userProfile'),
    path('DetailUserProfile/<int:pk>',DetailUserProfile.as_view(), name='DetailUserProfile'),
    path('createNumberMembership/<int:id>',createNumberMembership, name='createNumberMembership'),
]