from .views import HomePageView, AboutPageView, ContactUsPage
from django.views.generic.detail import DetailView
from django.urls import path
from main import views, models

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', views.ContactUsPage.as_view(), name=' contact '),
    path("products/<slug:slug>/", DetailView.as_view(model=models.Product), name="product", ),
    path("products/<slug:tag>/", views.ProductListView.as_view(), name="products"),
    path("products/", views.AllProductsView.as_view(), name='product'),

]
