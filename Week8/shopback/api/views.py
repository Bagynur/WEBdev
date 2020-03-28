from django.http.response import HttpResponse, JsonResponse

from api.models import Product, Category

def category_list(request):
    categories = Category.objects.all()
    category_json = [category.to_category_json() for category in categories]
    return JsonResponse(category_json, safe=False)

def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': 'category doesn`t exist'})
    return JsonResponse(category.to_category_json())

def products_from_category(request, category_id):
        products = Product.objects.all()
        len_products = len(products)
        product = []
        for i in range(len_products):
            if products[i].category_id.id == category_id:
                product.append(products[i])
        products_json = [x.to_product_json() for x in product]
        if(len(products_json) != 0):
            return JsonResponse(products_json, safe=False)
        else:
            return  JsonResponse({'error': 'category doesn`t exist'})

def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_product_json() for product in products]
    return JsonResponse(products_json, safe=False)

def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': 'product doesn`t exists'})
    return JsonResponse(product.to_product_json())