from django.conf.urls import url

from .views import (
    ComponentDetailView,
    ComponentIndexView
)


urlpatterns = [
    url(
        r'^$',
        ComponentIndexView.as_view(),
        name='component_index'
    ),
    url(
        (
            r'^(?P<group>[-\w\d]+)'
            '/(?P<component>[-\w\d]+)/'
        ),
        ComponentDetailView.as_view(),
        name='component_detail'
    )
]
