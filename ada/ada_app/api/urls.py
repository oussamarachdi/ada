from django.urls import path
from .views import ProductRudView, ProductAPIView, CategoryRudView, SubCategoryRudView, ProfileRudView, MyWishListRudView, ProductImageRudView, RegionRudView, MyProductRudView


urlpatterns = [
    path('product/', ProductAPIView.as_view(), name='product-create'),
    path('product/<name>/', ProductRudView.as_view(), name='product-rud'),
    path('category/<name>/', CategoryRudView.as_view(), name='category-rud'),
    path('subcategory/<name>/', SubCategoryRudView.as_view(), name='subcategory-rud'),
    path('profile/<id>/', ProfileRudView.as_view(), name='profile-rud'),
    path('mywishlist/<name>/', MyWishListRudView.as_view(), name='mywishlist-rud'),
    path('myproduct/<name>/', MyProductRudView.as_view(), name='myproduct-rud'),
    path('image/<name>/', ProductImageRudView.as_view(), name='productimage-rud'),
    path('region/<name>/', RegionRudView.as_view(), name='region-rud'),
]