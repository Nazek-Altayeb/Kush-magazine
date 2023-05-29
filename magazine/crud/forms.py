from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


"""   title = forms.CharField()
    body = forms.CharField()
    topics = forms.ModelChoiceField(
        queryset=Topic.objects.values_list('topic', flat=True).distinct())"""
