import os

from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import (
    override_settings,
    TestCase,
)
from systemfixtures import FakeFilesystem


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


@override_settings(BASE_DIR='/base', TEMPLATES=TEST_TEMPLATES)
class TestComponentIndexView(TestCase):

    def test_url_resolves(self):
        """"
        URL resolves as expected
        """
        url = reverse('components:component_index')

        self.assertEqual(url, '/components/')

    def test_get(self):
        """"
        GET request uses template
        """
        filesystem = FakeFilesystem()
        filesystem.setUp()
        filesystem.add('/base')
        os.mkdir('/base')
        os.mkdir('/base/templates')
        os.mkdir('/base/templates/components')
        os.mkdir('/base/templates/components/group1')
        os.mkdir('/base/templates/components/group2')
        os.mkdir('/base/templates/components/group1/Header')
        os.mkdir('/base/templates/components/group1/Footer')
        os.mkdir('/base/templates/components/group1/Header/demo')
        os.mkdir('/base/templates/components/group1/Footer/demo')
        open(
            '/base/templates/components/group1/Footer/demo/demo.html', 'a'
        ).close()
        open(
            '/base/templates/components/group1/Header/demo/demo.html', 'a'
        ).close()

        url = reverse('components:component_index')

        response = self.client.get(url)

        self.assertTemplateUsed(response, 'components/components_index.html')
        self.assertIn('components', response.context)
        components = response.context['components']
        self.assertEqual(
            len(components),
            1
        )
        self.assertIn('components', components[0])
        self.assertIn('Footer', components[0]['components'])
        self.assertIn('Header', components[0]['components'])
        self.assertEqual(components[0]['dir'], 'group1')
