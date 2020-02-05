from django.db import models


class Article(models.Model):
    title = models.TextField(verbose_name = 'Заголовок')
    text = models.TextField(verbose_name = 'Текст')
    published_at = models.DateTimeField(verbose_name = 'Дата создания подборки')

    class Meta:
        verbose_name = 'Статья с подборкой товаров'
        verbose_name_plural = 'Статьи с подборкой товаров'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'Название товара')
    img = models.FileField(upload_to = 'static')
    article = models.ForeignKey(Article, blank = True, null = True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Review(models.Model):
    MARK_CHOICES = (
        (1, ★),
        (2, ★★),
        (3, ★★★),
        (4, ★★★★),
        (5, ★★★★★),
    )
    customer_name = models.CharField(max_length = 50, verbose_name = 'Имя')
    review_text = models.TextField(verbose_name = 'Содержание отзыва')
    mark = models.Charfield(max_length = 1, choices = MARK_CHOICES, verbose_name = 'Рейтинг')
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    def __str__(self):
        return self.review_text[:50]

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'