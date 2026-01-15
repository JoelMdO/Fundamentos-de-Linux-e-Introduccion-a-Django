from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import ProductModel
from django.contrib.auth.decorators import login_required
from .forms import ProductModelForm
from .models import ProductModel
from django.db.models import Q

# Create your views here.
#@login_required(login_url='/admin/login/')
##--------------------------------------------------------
## CREATE VIEW
##--------------------------------------------------------
def product_model_create_view(request: HttpRequest) -> HttpResponse:
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Produto creado con exito.")
        return HttpResponseRedirect("/ecommerce/{product_id}/".format(product_id=instance.id))
    template = "ecommerce/product_create.html"
    context = {"form": form}
    return render(request, template, context)

##--------------------------------------------------------
## DETAIL VIEW (ONE PRODUCT)
##--------------------------------------------------------
def product_model_detail_view(request: HttpRequest, product_id: int) -> HttpResponse:
    instance = get_object_or_404(ProductModel, id=product_id)
    template = "ecommerce/product_detail.html"
    context = {"product": instance}
    
    return render(request, template, context)

##--------------------------------------------------------
## PRODUCTS LIST VIEW WITH LOGIN REQUIRED
##--------------------------------------------------------
@login_required(login_url='/admin/login/')
def product_model_list_view(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("q", None)
    queryset = ProductModel.objects.all()
    if query is not None:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
    products = queryset
    template = "ecommerce/product_list.html"
    context = {"products": products}
    
    if request.user.is_authenticated:
        template = "ecommerce/product_list.html"
    else:
        template = "ecommerce/product_list_public.html"
    
    return render(request, template, context)
##--------------------------------------------------------
## UPDATE VIEW
##--------------------------------------------------------
def product_model_update_view(request: HttpRequest, product_id: int) -> HttpResponse:
    instance = get_object_or_404(ProductModel, id=product_id)
    form = ProductModelForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Produto actualizado con exito.")
        return HttpResponseRedirect("/ecommerce/{product_id}/".format(product_id=instance.id))
    template = "ecommerce/product_update.html"
    context = {"form": form}
    return render(request, template, context)
##--------------------------------------------------------
## DELETE VIEW (ONE PRODUCT)
##--------------------------------------------------------
def product_model_delete_view(request: HttpRequest, product_id: int) -> HttpResponse:
    instance = get_object_or_404(ProductModel, id=product_id)
    if request.method == "POST":
        instance.delete()
        messages.success(request, "Produto eliminado con exito.")
        return HttpResponseRedirect("/ecommerce/")
    template = "ecommerce/product_delete.html"
    context = {"product": instance}
    
    return render(request, template, context)
#    return render(request, "ecommerce/product_list.html", {"products": products})

# def home(request: HttpRequest) -> HttpResponse:
#     html = """
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>E-commerce Home</title>
#     </head>
#     <body>
#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             background-color: #f4f4f4;
#             margin: 0;
#             padding: 20px;
#         }
#         h1 {
#             color: #333;
#         }
#     </style>
#     <h1>Welcome to the E-commerce Home Page
#     </h1>
#     </body>
#     </html>
# """
#     return HttpResponse(html)

# def HomeView(request: HttpRequest) -> HttpResponse:
#     return render(request, "ecommerce/home.html")

# def Home(request: HttpRequest) -> HttpResponse:
#     response = HttpResponse()
#     response.write("<html><body><h1>E-commerce Home Page</h1></body></html>")
#     return response

# def redirect_to_home(request: HttpRequest) -> HttpResponse:
#     return HttpResponseRedirect("/ecommerce")