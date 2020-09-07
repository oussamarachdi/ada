from ada_app.models import Category, SubCategory, Product, MyProduct, MyWishList, ProductImage, Profile, Region
from .serializers import CategorySerializer, SubCategorySerializer, ProductSerializer, MyProductSerializer, MyWishListSerializer, ProductImageSerializer, ProfileSerializer, RegionSerializer
from rest_framework import generics


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryList(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class ProductList(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class MyProductList(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class MyProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyProduct.objects.all()
    serializer_class = MyProductSerializer

class MyWishList_List(generics.ListCreateAPIView):
    queryset = MyWishList.objects.all()
    serializer_class = MyWishListSerializer


class MyWishListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyWishList.objects.all()
    serializer_class = MyWishListSerializer

class ProductImageList(generics.ListCreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class ProductImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class RegionList(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer