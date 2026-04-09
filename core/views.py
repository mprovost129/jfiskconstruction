from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'core/home.html'


class ProductsView(TemplateView):
    template_name = 'core/products.html'


class ServicesView(TemplateView):
    template_name = 'core/services.html'


class AboutView(TemplateView):
    template_name = 'core/about.html'


class ContactView(TemplateView):
    template_name = 'core/contact.html'
