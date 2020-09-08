from django.contrib import admin
#from django.contrib.auth.models import Group
from ada_app.model import (Product,
                           ProductImage,
                           SubCategory,
                           Category,
                           Profile,
                           Region,
                           MyWishList,
                           MyProduct)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'creationdate')
    list_filter = ('creationdate',)


admin.site.site_header = 'ADA ADMIN'
#admin.site.unregister(Group)
admin.site.register(Profile)
admin.site.register(ProductImage)
admin.site.register(Product, ProductAdmin)
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(MyWishList)
admin.site.register(MyProduct)
admin.site.register(Region)
