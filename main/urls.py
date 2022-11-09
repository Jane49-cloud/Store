from .views import HomePageView, AboutPageView, ContactUsPage
from django.contrib.auth import views as auth_views
from django.views.generic.detail import DetailView
from django.urls import path
from main import views, models, forms

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', views.ContactUsPage.as_view(), name=' contact '),
    path("products/<slug:slug>/", DetailView.as_view(model=models.Product), name="product", ),
    path("products/<slug:tag>/", views.ProductListView.as_view(), name="products"),
    path("products/", views.AllProductsView.as_view(), name='product'),
    path('login/', auth_views.LoginView.as_view(
        template_name="login.html",
        form_class=forms.AuthenticationForm,
    ), name="login")

]
