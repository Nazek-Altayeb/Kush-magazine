from django.shortcuts import render
from .models import Article

# Create your views here.


def get_article(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'crud/get_article.html', context)


def add_article(request):
    return render(request, 'crud/add_article.html')
