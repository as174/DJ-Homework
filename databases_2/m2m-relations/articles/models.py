from django.db import models


class Scope(models.Model):

    topic = models.CharField(max_length=256, verbose_name='Раздел')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['topic']

    def __str__(self):
        return self.topic


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    scopes = models.ManyToManyField(Scope, through='ArticleScope', related_name='tags')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class ArticleScope(models.Model):

    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    scope = models.ForeignKey('Scope', on_delete=models.CASCADE, verbose_name='Раздел')
    is_main = models.BooleanField(default=False, verbose_name='Главный раздел')

    class Meta:
        ordering = ['-is_main','scope']


