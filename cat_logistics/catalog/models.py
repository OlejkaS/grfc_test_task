from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """Модель для формирования категорий.

    Attributes:
        name (str): Название категории.
        parent (Category): Родительская категория (если она есть).
    """
    name = models.CharField('Название', max_length=50, db_index=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_index=True,
        related_name='children',
        verbose_name='Родительская категория'
    )

    class MPTTMeta:
        order_insertion_by = ('name',)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
