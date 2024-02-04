from rest_framework import serializers
from .models import Product
 
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')



class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        # Check if data is a list of items
        if isinstance(validated_data, list):
            # Create a list to store the created products
            created_products = []

            # Iterate through each item in the list and create a Product
            for data in validated_data:
                created_products.append(Product.objects.create(**data))
            
            return " created succesfully "
        else:
            # If it's not a list, create a single Product
            return Product.objects.create(**validated_data)