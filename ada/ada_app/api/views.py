from ada_app.models import Category, SubCategory, Product, MyProduct, MyWishList, ProductImage, Profile, Region
from .serializers import (CategoryListSerializer, CategoryWriteSerializer, 
                          SubCategoryListSerializer, SubCategoryWriteSerializer, 
                          ProductListSerializer, ProductWriteSerializer,
                          MyProductListSerializer, MyProductWriteSerializer, 
                          MyWishListWriteSerializer, MyWishListReadSerializer, 
                          ProductImageReadSerializer, ProductImageWriteSerializer,
                          ProfileListSerializer, ProfileWriteSerializer,
                          RegionReadSerializer, RegionWriteSerializer)
from rest_framework import generics


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryWriteSerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

class SubCategoryList(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryWriteSerializer


class SubCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryListSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWriteSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class MyProductList(generics.ListCreateAPIView):
    queryset = MyProduct.objects.all()
    serializer_class = MyProductWriteSerializer


class MyProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyProduct.objects.all()
    serializer_class = MyProductListSerializer

class MyWishList_List(generics.ListCreateAPIView):
    queryset = MyWishList.objects.all()
    serializer_class = MyWishListWriteSerializer


class MyWishListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyWishList.objects.all()
    serializer_class = MyWishListReadSerializer

class ProductImageList(generics.ListCreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageWriteSerializer


class ProductImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageReadSerializer

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileWriteSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer

class RegionList(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionWriteSerializer


class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionReadSerializer