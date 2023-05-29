from django import forms
from .models import Topic, Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField()
    body = forms.CharField()
    topics = forms.ModelChoiceField(
        queryset=Topic.objects.values_list('topic', flat=True).distinct())

    class Meta:
        model = Article
        fields = ('title', 'body', 'topic',)
