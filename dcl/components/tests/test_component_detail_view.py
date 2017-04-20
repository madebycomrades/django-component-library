import os
from unittest.mock import (
    patch,
    mock_open,
)

from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import (
    override_settings,
    TestCase,
)

TEST_TEMPLATE_DIR = os.path.join(
    settings.BASE_DIR, 'components/tests/templates'
)
TEST_TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEST_TEMPLATE_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


@override_settings(TEMPLATES=TEST_TEMPLATES)
class TestComponentDetailView(TestCase):

    def test_url_resolves(self):
        """"
        URL resolves as expected
        """
        url = reverse(
            'components:component_detail',
            kwargs={'group': 'global', 'component': 'Footer'}
        )

        self.assertEqual(url, '/components/global/Footer/')

    def test_get(self):
        """"
        GET request uses template
        """
        url = reverse(
            'components:component_detail',
            kwargs={'group': 'global', 'component': 'Footer'}
        )

        data = '{"test":"test"}'

        with patch('builtins.open', mock_open(read_data=data)):
            response = self.client.get(url)

            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(
                response, 'components/global/Footer/demo/demo.html'
            )
            self.assertEqual(response.context['data'], {'test': 'test'})
