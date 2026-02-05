from django.http import JsonResponse
from .models import Product

def product_list(request):
    products=Product.objects.all()
    
    data=[]
    for product in products:
        data.append({
            "id":product.id,
            "name":product.name,
            "price":product.price,
            "qty":product.quantity,
        })
        
        return JsonResponse(data,safe=False)
