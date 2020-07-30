from django.contrib import admin
from .models import Product, ProductImage, SubCategory, Category, Profile, Region, MyWhishList

admin.site.register(Profile)
admin.site.register(ProductImage)
admin.site.register(Product)
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(MyWhishList)
