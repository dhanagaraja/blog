"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import HomeView,ArticleDetailView,AddPostView,UpdatePostView, DeletePostView, AddCategoryView,CategoryView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='detail-view'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('add-post/<int:pk>/edit/', UpdatePostView.as_view(), name='update-post'),
    path('delete-post/<int:pk>', DeletePostView.as_view(), name='delete-post'),
    path('add-category/', AddCategoryView.as_view(), name="add-category"),
    path('category/<str:cats>/', CategoryView, name="view-category"),
]
