from django.urls import reverse_lazy

from .models import Category


class CategoryModelMixin:
    model = Category


class SuccessUrlMixin:
    success_url = reverse_lazy('index')
