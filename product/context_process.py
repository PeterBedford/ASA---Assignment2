
from product.models import Product


def get_product_names(request):
        return {
            'products': Product.objects.all()
        }
    

    
