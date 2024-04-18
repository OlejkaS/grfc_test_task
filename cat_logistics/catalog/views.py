from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import CategoryForm
from .mixins import CategoryModelMixin, SuccessUrlMixin


class CategoryCreateView(CategoryModelMixin, SuccessUrlMixin, CreateView):
    """Представление для создания новой категории.

    Attributes:
        fields (tuple[str]): Поля формы для создания категории (name, parent).
    """

    fields: tuple[str] = ('name', 'parent')


class CategoryListView(CategoryModelMixin, ListView):
    """Представление для отображения списка категорий.

    Attributes:
        template_name (str): Шаблон для отображения страницы списка категорий.
        context_object_name (str): Имя переменной контекста.
        extra_context (dict[str, CategoryForm]): Дополнительный контекст для передачи в шаблон.
    """

    template_name: str = 'catalog/index.html'
    context_object_name: str = 'categories'
    extra_context: dict[str, CategoryForm] = {'form': CategoryForm}


class CategoryDetailView(CategoryModelMixin, DetailView):
    """Представление для отображения страницы категории.

    Attributes:
        template_name (str): Имя шаблона для отображения страницы категории.
        context_object_name (str): Имя переменной контекста.
    """

    template_name: str = 'catalog/category.html'
    context_object_name: str = 'category'


class CategoryDeleteView(CategoryModelMixin, SuccessUrlMixin, DeleteView):
    """Представление для удаления категории."""

    pass


class CategoryUpdateView(CategoryModelMixin, UpdateView):
    """Представление для обновления категории.

    Attributes:
        fields (tuple[str]): Поля формы для обновления категории (только name).
    """

    fields: tuple[str] = ('name',)

    def get_success_url(self) -> str:
        return reverse_lazy('category_page', kwargs={'pk': self.object.pk})
