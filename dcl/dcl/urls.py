from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from .views import HomeView

urlpatterns = [

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),

    url(r'^components/', include('components.urls', namespace='components')),

    url(r'^articles/', include('articles.urls', namespace='articles')),
]
