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
        list_display = ('name', 'creationdate','category','subcategory')
        list_filter = ('creationdate',)
        search_fields = ('name__exact',)

        def get_ordering(self, request):
            if request.user.is_superuser:
                return ('name', 'creationdate',)

            return  ('name',)

class CategoryAdmin(admin.ModelAdmin):
        list_display = ('name','numberOfSearchRequests')
        list_filter = ('name',)
        search_fields = ('name__exact',)

        def get_ordering(self, request):
            if request.user.is_superuser:
                return ('name', 'numberOfSearchRequests')
            return ('name',)

class ProfileAdmin(admin.ModelAdmin):
        list_display = ('name','user', 'email')
        list_filter = ('id',)
        search_fields = ('name__exact',)

        def get_ordering(self, request):
            if request.user.is_superuser:
                return ('name','user', 'email')
            return ('name',)

class ProductImageAdmin(admin.ModelAdmin):
        list_display = ('name','product')
        list_filter = ('name',)
        search_fields = ('name__exact',)

        def get_ordering(self, request):
            if request.user.is_superuser:
                return ('name','product',)
            return ('name',)
class SubCategoryAdmin(admin.ModelAdmin):
        list_display = ('name','category')
        list_filter = ('name',)
        search_fields = ('name__exact',)

        def get_ordering(self, request):
            if request.user.is_superuser:
                return ('name','category',)
            return ('name',)
class MyWishListAdmin(admin.ModelAdmin):
        list_display = ('name','user')
        list_filter = ('name',)
        search_fields = ('name__exact',)

        def get_ordering(self, request):
            if request.user.is_superuser:
                return ('name','user',)
            return ('name',)
class MyProductAdmin(admin.ModelAdmin):
        list_display = ('name','myproduct')
        list_filter = ('name',)
        search_fields = ('name__exact',)

        def get_ordering(self, request):
            if request.user.is_superuser:
                return ('name','myproduct',)
            return ('name',)

class RegionAdmin(admin.ModelAdmin):
        list_display = ('name',)
        list_filter = ('name',)
        search_fields = ('name__exact',)

admin.site.site_header = 'Ada Admin'
admin.site.site_title = 'Ada Admin'
admin.site.index_title = 'Ada Administration'
#admin.site.unregister(Group)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(MyWishList, MyWishListAdmin)
admin.site.register(MyProduct, MyProductAdmin)
admin.site.register(Region, RegionAdmin)
