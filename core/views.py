from datetime import date

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'core/home.html'


class ProductsView(TemplateView):
    template_name = 'core/products.html'


class ServicesView(TemplateView):
    template_name = 'core/services.html'


class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['years_in_business'] = date.today().year - 1975
        return context


class ContactView(TemplateView):
    template_name = 'core/contact.html'
