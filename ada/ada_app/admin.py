from django.contrib import admin
from ada_app.model import Product, ProductImage, SubCategory, Category, Profile, Region, MyWishList

admin.site.register(Profile)
admin.site.register(ProductImage)
admin.site.register(Product)
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(MyWishList)
