from django.urls import path

from .views import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryDetailView,
    CategoryListView,
    CategoryUpdateView
)

urlpatterns = [
    path('', CategoryListView.as_view(), name='index'),
    path(
        'create_category/',
        CategoryCreateView.as_view(),
        name='create_category'
    ),
    path(
        'category/<int:pk>/',
        CategoryDetailView.as_view(),
        name='category_page'
    ),
    path(
        'category/<int:pk>/delete/',
        CategoryDeleteView.as_view(),
        name='delete_category'
    ),
    path(
        'category/<int:pk>/update/',
        CategoryUpdateView.as_view(),
        name='update_category'
    )
]
