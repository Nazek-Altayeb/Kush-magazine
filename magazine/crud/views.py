from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Topic
from .forms import ArticleForm
# from .forms import DropDown

# Create your views here.


def get_article(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/get_article.html', context)


def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_article')
    form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/add_article.html', context)


def get_topic(request):
    topics = Topic.objects.all()
    context = {
        'topics': topics
    }
    return render(request, 'topics/get_topic.html', context)


def add_topic(request):
    if request.method == "POST":
        topic_name = request.POST.get('topic_name')

        Topic.objects.create(name=topic_name)
        return redirect('get_topic')
    return render(request, 'topics/add_topic.html')


def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('get_article')
    form = ArticleForm(instance=article)
    context = {
        'form': form
    }
    return render(request, 'articles/edit_article.html', context)


def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('get_article')
