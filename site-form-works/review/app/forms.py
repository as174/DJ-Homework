from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='Отзыв', required=True)

    class Meta(object):
        model = Review
        exclude = ('id', 'product')
