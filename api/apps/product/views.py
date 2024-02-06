from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer , ProductCreateSerializer, ProductSearchSerializer
from rest_framework.response import Response
from .filters import ProductFilter
from django.db.models import Q


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

class ProductSearchListAPIView(generics.ListAPIView):
    serializer_class = ProductSearchSerializer

    def get_queryset(self):
        search_value = self.request.query_params.get('search', '')
        queryset = Product.objects.all()
        print(search_value , "search value")
        print(queryset , "queryset")
        if search_value:
            queryset = queryset.filter(
                Q(title__icontains=search_value) |
                Q(description__icontains=search_value)
            )
        return queryset

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer

    def create(self, request, *args, **kwargs):
        # If the request data is a list, set many=True for the serializer
        many = isinstance(request.data, list)
        
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Return the serialized data
        if many:
            return Response(serializer.data, status=201)
        else:
            return super().create(request, *args, **kwargs)

class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer