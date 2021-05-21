from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class ProductPageView(ListView):
    model = Product
    template_name = 'product_list.html'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'product_update.html'
    fields = ['name','detail','price']



class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('home')


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'product_new.html'
    fields = ('name','detail','price','Image')