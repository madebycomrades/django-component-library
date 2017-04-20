from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self,  **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['DemoHeader'] = {
            'nav_items': [
                {
                    'label': 'Home',
                    'url': '/',
                    'active': True
                },
                {
                    'label': 'About',
                    'url': '/about',
                    'active': False
                },
                {
                    'label': 'Services',
                    'url': '/services',
                    'active': False
                }
            ]
        }
        context['DemoList'] = [
            {
                "label": "Lorem",
                "url": "#lorem"
            },
            {
                "label": "Ipsum",
                "url": "#ipsum"
            },
            {
                "label": "Dolor",
                "url": "#dolor"
            },
            {
                "label": "Sit amet",
                "url": "#sit-amet"
            }
        ]

        return context
