from django.contrib import admin
from product.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name', 'brand', 'average_cost', 'category', 'date_released')

class ReviewAdmin(admin.ModelAdmin):
    search_fields = ('Author', 'Product', 'rating', 'description', 'date_posted')


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
