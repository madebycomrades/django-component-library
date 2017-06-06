from django.views.generic import TemplateView

from .models import Article
from .serializers import ArticleDemoThumbSerializer


class ArticlesView(TemplateView):
    template_name = 'articles.html'

    def get_context_data(self, **kwargs):
        context = super(ArticlesView, self).get_context_data(**kwargs)
        articles = Article.objects.all()
        articles_serializer = ArticleDemoThumbSerializer(
            articles, many=True
        )
        context['articles'] = articles_serializer.data
        return context
