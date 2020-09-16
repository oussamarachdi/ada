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
        search_fields = ('name__exact',)

        def get_ordering(self, request):
            if request.user.is_superuser:
                return ('name', 'creationdate',)

            return  ('name',)

admin.site.site_header = 'Ada Admin'
admin.site.site_title = 'Ada Admin'
admin.site.index_title = 'Ada Administration'
#admin.site.unregister(Group)
admin.site.register(Profile)
admin.site.register(ProductImage)
admin.site.register(Product, ProductAdmin)
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(MyWishList)
admin.site.register(MyProduct)
admin.site.register(Region)
