from typing import Optional

from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """Модель для формирования категорий.

    Attributes:
        name (str): Название категории.
        parent (Optional): Родительская категория (если она есть).
    """
    name: str = models.CharField('Название', max_length=50, db_index=True)
    parent: Optional['Category'] = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_index=True,
        related_name='children',
        verbose_name='Родительская категория'
    )

    class MPTTMeta:
        order_insertion_by: tuple[str] = ('name',)

    class Meta:
        verbose_name: str = 'Категория'
        verbose_name_plural: str = 'Категории'

    def __str__(self) -> str:
        return self.name
