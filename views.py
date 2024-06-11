from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import categoryTable
from .models import categoryTable, ProductModel


# Create your views here.

# def product_list(request):
 #   return HttpResponse("This page will show a list of products.")
#def categories_list(request, prod):
   # if prod== "car":
       # return HttpResponseNotFound("This page is not exist.")
 #  return HttpResponse("This page will show a list of "+prod+" products.")
# def digital(request):
#    return HttpResponse("This page will show a list of Digital products.")
# def kitchen(request):
#    return HttpResponse("This page will show a list of Kitchen products")


# def category_list(request, prod):
#     context = {
#         "cluster_name": prod
#     }
#     if prod == "car":
#         raise Http404()
#     return render(request, '
#     productsList.html', context)
# def index(request):
#     return HttpResponse("This page will show a list of products.")

def categoreisView(request):
    categoreis = categoryTable.objects.all()
    return render(request, 'HomePage.html', {'categs': categoreis})

def productsView(request, categoryName):
    products = ProductModel.objects.filter(category__name=categoryName)
    categoryRecord = categoryTable.objects.get(name=categoryName)
    return render(request, 'productsList.html', {'prods': products, 'categ_name': categoryRecord.name})


from django.http import JsonResponse

def products_list(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category_name = request.POST.get('category_name')

        # انجام عملیات مرتبط با دسته‌بندی در اینجا

        return JsonResponse({'message': f'Received category: {category_name}'})