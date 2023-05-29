from django.shortcuts import render, redirect
from .models import Article, Topic
from .forms import ArticleForm
# from .forms import DropDown

# Create your views here.


"""def get_article(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'crud/get_article.html', context)"""


def add_article(request):
    if request.method == "POST":
        article_title = request.POST.get('article_title')
        article_body = request.POST.get('article_body')
        article_topic = request.POST.get('article_topic')
        Article.objects.create(title=article_title,
                               body=article_body, topic=article_topic)
        return redirect('get_article')
    return render(request, 'crud/add_article.html')


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


def get_article(request):
    form = ArticleForm()
    # topics = Topic.objects.all()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
       # form = ArticleForm(request.POST, instance=Article.objects.first())
        if form.is_valid():
            form.save()
            return redirect('get_article')
    return render(request, 'crud/add_article.html', {'form': form})
