import os
from datetime import date

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView


SITE_URL = os.environ.get('SITE_URL', 'https://www.jfiskconstruction.com').rstrip('/')
SERVICE_AREAS = [
    'Attleboro, MA',
    'New Bedford, MA',
    'Providence, RI',
    'Barrington, RI',
    'Massachusetts',
    'Rhode Island',
]
OPENING_HOURS = [
    {
        'days': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
        'opens': '07:00',
        'closes': '15:30',
    },
    {
        'days': ['Saturday'],
        'opens': '07:00',
        'closes': '12:00',
    },
]


class SeoTemplateView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'site_url': SITE_URL,
                'canonical_url': f'{SITE_URL}{self.request.path}',
                'business_phone_display': '(508) 399-8570',
                'business_phone_link': '+15083998570',
                'business_street_address': '68 Woodland Avenue',
                'business_city': 'Seekonk',
                'business_state': 'MA',
                'business_postal_code': '02771',
                'service_areas': SERVICE_AREAS,
                'opening_hours': OPENING_HOURS,
            }
        )
        return context


class HomeView(SeoTemplateView):
    template_name = 'core/home.html'


class ProductsView(SeoTemplateView):
    template_name = 'core/products.html'


class ServicesView(SeoTemplateView):
    template_name = 'core/services.html'


class AboutView(SeoTemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['years_in_business'] = date.today().year - 1975
        return context


class ContactView(SeoTemplateView):
    template_name = 'core/contact.html'


def robots_txt(request):
    lines = [
        'User-agent: *',
        'Allow: /',
        f'Sitemap: {SITE_URL}/sitemap.xml',
    ]
    return HttpResponse('\n'.join(lines), content_type='text/plain')


def sitemap_xml(request):
    pages = [
        {'location': f'{SITE_URL}/', 'priority': '1.0'},
        {'location': f'{SITE_URL}/products/', 'priority': '0.9'},
        {'location': f'{SITE_URL}/services/', 'priority': '0.9'},
        {'location': f'{SITE_URL}/about/', 'priority': '0.7'},
        {'location': f'{SITE_URL}/contact/', 'priority': '0.8'},
    ]
    xml = render_to_string('sitemap.xml', {'pages': pages}, request=request)
    return HttpResponse(xml, content_type='application/xml')
