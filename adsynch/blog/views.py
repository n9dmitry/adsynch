from django.shortcuts import render
from .models import Article
from django.views.generic import DetailView
def articlelist(request):
    published_articles = Article.objects.filter(published=True)  # Фильтрация опубликованных статей

    context = {
        'published_articles': published_articles
    }
    return render(request, 'blog/article.html', context)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'  # Используйте 'article' вместо 'published_articles'