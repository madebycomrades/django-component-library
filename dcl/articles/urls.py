from django.conf.urls import url

from .views import ArticlesView

app_name = 'articles'

urlpatterns = [
    url(r'^$', ArticlesView.as_view(), name='articles'),
]
