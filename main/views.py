from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from main import forms
from main import models


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactUsPage(FormView):
    template_name = 'forms.html'
    form_class = forms.ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)


class ProductListView(ListView):
    template_name = 'product_list.html'
    paginate_by = 4

    def get_queryset(self):
        tag = self.kwargs['tag']
        self.tag = None
        if tag != "all":
            self.tag = get_object_or_404(
                models.ProductTag, slug=tag
            )
        if self.tag:
            products = models.Product.objects.filter(
                tags=self.tag)
        else:
            products = models.Product.objects.all()
        return products.order_by('name')


class AllProductsView(ListView):
    template_name = 'product_list.html'
    paginate_by = 4

    def get_queryset(self):
        products = models.Product.objects.all()
        return products.order_by('name')
