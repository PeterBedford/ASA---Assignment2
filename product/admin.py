from django.contrib import admin
from product.models import Product, Review, Manufacturer


class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name', 'brand', 'average_cost', 'category', 'date_released')

class ReviewAdmin(admin.ModelAdmin):
    search_fields = ('Author', 'Product', 'rating', 'description', 'date_posted')

class ManufacturerAdmin(admin.ModelAdmin):
    search_fields = ('name', 'industry')

admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)