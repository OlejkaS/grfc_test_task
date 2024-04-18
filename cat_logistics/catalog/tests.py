from django.test import TestCase
from django.urls import reverse

from .forms import CategoryForm
from .models import Category


class CategoryFormTestCase(TestCase):
    def test_valid_category_form(self):
        form_data = {'name': 'Test Category'}
        form = CategoryForm(data=form_data)
        self.assertTrue(form.is_valid())


class CategoryModelTestCase(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name='Test Category')
        self.assertTrue(isinstance(category, Category))
        self.assertEqual(category.__str__(), category.name)

    def test_category_deletion(self):
        category = Category.objects.create(name='Test Category')
        category.delete()
        self.assertEqual(Category.objects.count(), 0)


class CategoryViewsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_category_list_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.category.name)

    def test_category_detail_view(self):
        response = self.client.get(
            reverse(
                'category_page',
                args=[self.category.pk]
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.category.name)


class CategoryUrlsTestCase(TestCase):
    def test_category_list_url(self):
        url = reverse('index')
        self.assertEqual(url, '/')

    def test_category_create_url(self):
        url = reverse('create_category')
        self.assertEqual(url, '/create_category/')

    def test_category_detail_url(self):
        category = Category.objects.create(name='Test Category')
        url = reverse('category_page', args=[category.id])
        self.assertEqual(url, f'/category/{category.id}/')

    def test_category_delete_url(self):
        category = Category.objects.create(name='Test Category')
        url = reverse('delete_category', args=[category.id])
        self.assertEqual(url, f'/category/{category.id}/delete/')

    def test_category_update_url(self):
        category = Category.objects.create(name='Test Category')
        url = reverse('update_category', args=[category.id])
        self.assertEqual(url, f'/category/{category.id}/update/')
