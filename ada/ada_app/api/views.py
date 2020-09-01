from rest_framework import generics
from ada_app.models import Product, Category, MyProduct, MyWishList, ProductImage, Profile, Region, SubCategory
from .serializers import ProductSerializer, CategorySerializer, SubCategorySerializer, MyProductSerializer, MyWishListSerializer, ProfileSerializer, RegionSerializer, ProductImageSerializer

class ProductRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'name'
    serializer_class = ProductSerializer
    def get_queryset(self):
        return Product.objects.all()

    #def get_object(self):
    #    pk = self.kwargs.get("pk")
    #    return Product.objects.get(pk=pk)

class ProductAPIView(generics.CreateAPIView):
    lookup_field = 'name'
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

class CategoryRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'name'
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.all()

class CategoryAPIView(generics.CreateAPIView):
    lookup_field = ''
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

class SubCategoryRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'name'
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        return SubCategory.objects.all()

class SubCategoryAPIView(generics.CreateAPIView):
    lookup_field = ''
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        return SubCategory.objects.all()

class MyProductRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'name'
    serializer_class = MyProductSerializer

    def get_queryset(self):
        return MyProduct.objects.all()

class MyProductAPIView(generics.CreateAPIView):
    lookup_feild = ''
    serializer_class = MyProductSerializer
    def get_queryset(self):
        return MyProduct.objects.all()

class MyWishListRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'name'
    serializer_class = MyWishListSerializer

    def get_queryset(self):
        return MyWishList.objects.all()

class MyWishListAPIView(generics.CreateAPIView):
    lookup_field = ''
    serializer_class = MyWishListSerializer
    def get_queryset(self):
        return MyWishList.objects.all()

class ProfileRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.all()

class ProfileAPIView(generics.CreateAPIView):
    lookup_field = ''
    serializer_class = ProfileSerializer
    def get_queryset(self):
        return Profile.objects.all()

class RegionRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'name'
    serializer_class = RegionSerializer

    def get_queryset(self):
        return Region.objects.all()

class RegionAPIView(generics.CreateAPIView):
    lookup_field = ''
    serializer_class = RegionSerializer
    def get_queryset(self):
        return Region.objects.all()

class ProductImageRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'name'
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        return ProductImage.objects.all()

class ProductImageAPIView(generics.CreateAPIView):
    lookup_field = ''
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        return ProductImage.objects.all()