from django.urls import path
from .views import ProductPageView, ProductUpdateView, ProductDeleteView, ProductDetailView, ProductCreateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',ProductPageView.as_view(),name='home'),
    path('<int:pk>/',ProductDetailView.as_view(),name='detail'),
    path('<int:pk>/update/',ProductUpdateView.as_view(),name='update'),
    path('<int:pk>/delete/',ProductDeleteView.as_view(),name='delete'),
    path('new/',ProductCreateView.as_view(),name='new'),
]