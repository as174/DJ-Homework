from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScope

class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        selected_topics = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                selected_topics += 1
            if selected_topics > 1:
                raise ValidationError('Основным может быть только один раздел')
        if not selected_topics:
            raise ValidationError('Укажите основной раздел')
        return super().clean()

class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass