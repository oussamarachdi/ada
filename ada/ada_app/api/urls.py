from django.urls import path
from .views import CategoryList, CategoryDetail, SubCategoryList, SubCategoryDetail, ProductDetail, ProductList, MyProductDetail, MyProductList, MyWishList_List, MyWishListDetail, ProductImageDetail, ProductImageList, ProfileList, ProfileDetail, RegionList, RegionDetail


urlpatterns = [
    path('category/', CategoryList.as_view(), name='category-create'),
    path('category/<pk>/', CategoryDetail.as_view(), name='category-rud'),
    path('subcategory/', SubCategoryList.as_view(), name='subcategory-create'),
    path('subcategory/<pk>/', SubCategoryDetail.as_view(), name='subcategory-rud'),
    path('product/', ProductList.as_view(), name='product-create'),
    path('product/<pk>/', ProductDetail.as_view(), name='product-rud'),
    path('myproduct/', MyProductList.as_view(), name='myproduct-create'),
    path('myproduct/<pk>/', MyProductDetail.as_view(), name='myproduct-rud'),
    path('mywishlist/', MyWishList_List.as_view(), name='mywishlist-create'),
    path('mywishlist/<pk>/', MyWishListDetail.as_view(), name='mywishlist-rud'),
    path('productimage/', ProductImageList.as_view(), name='productimage-create'),
    path('productimage/<pk>/', ProductImageDetail.as_view(), name='productimage-rud'),
    path('profile/', ProfileList.as_view(), name='profile-create'),
    path('profile/<pk>/', ProfileDetail.as_view(), name='profile-rud'),
    path('region/', RegionList.as_view(), name='region-create'),
    path('region/<pk>/', RegionDetail.as_view(), name='region-rud'),
]