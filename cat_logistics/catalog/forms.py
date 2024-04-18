from django import forms

from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model: Category = Category
        fields: tuple[str] = ('name', 'parent')
