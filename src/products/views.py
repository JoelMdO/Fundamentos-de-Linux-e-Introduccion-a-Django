from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, View, TemplateView, RedirectView, DetailView, CreateView
#from django.views.decorators.http import require_http_methods
from django.forms.models import BaseModelForm

from src.ecommerce.forms import ProductModelForm
from .models import DigitalProduct, Product
from .mixins import TemplateTitleMixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# from .models import Product

# class ProductHomeView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, "products/home.html", {})
    
#     def post(self, request, *args, **kwargs):
#         return render(request, "products/home.html", {})

# class ProductListView(ListView):
#     queryset = Product.objects.all()

# product_list_view = require_http_methods(["GET"])(ProductListView.as_view())

# class BlogPostListView(ListView):
#     queryset = Post.objects.all()

# class AboutView(View):
#     def get(self, request):
#         return render(request, "about.html", {})

class ProductListView(TemplateTitleMixin, ListView):
    model = Product
    template_name = "products/product_list.html"
    title = "Product List"

    # With mixin, no need context data
    # def get_context_data(self, **args, **kwargs: Any) -> dict[str, Any]:
    #     return super().get_context_data(**args,**kwargs)

class ProductDetailView(View):
    model = Product

class DigitalProductListView(TemplateTitleMixin, ListView):
    model = DigitalProduct
    template = "products/digitalproduct_list.html"
    title = "Digital Product List"

    # With mixin, no need context data
    # def get_context_data(self, **args, **kwargs: Any) -> dict[str, Any]:
    #     return super().get_context_data(**args,**kwargs)

class AboutView(TemplateView):
    template_name = "about.html"

def about_us_redirect_view(request: HttpRequest) -> HttpResponseRedirect:
    return HttpResponseRedirect("/about/")

class AboutUsRedirectView(RedirectView):
    url = "/about/"

##--------------------------------------------------------
## Redirect baased on Model instance
##--------------------------------------------------------
class ProductRedirectView(RedirectView):

    def get_redirect_url(self, *args: Any, **kwargs: Any) -> str:
        url_params = self.kwargs
        pk = url_params.get("pk")
        obj = get_object_or_404(Product, pk=pk)
        slug = obj.pk
        return f"/products/products/{slug}/"

##--------------------------------------------------------
## Mixin para proteger login
##--------------------------------------------------------
class ProtectedProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

###--------------------------------------------------------
## Create view
##--------------------------------------------------------
class ProtectedProductCreateView(LoginRequiredMixin, CreateView):
    form_class = ProductModelForm
    model = Product
    template_name = "products/product_form.html"
    success_url = "/products/"

    def form_valid(self, form: BaseModelForm):
        form.instance.user = self.request.user
        return super().form_valid(form)
###--------------------------------------------------------
## Protected List View
##--------------------------------------------------------
class ProtectedProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "products/protected_product_list.html"

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(user=self.request.user)