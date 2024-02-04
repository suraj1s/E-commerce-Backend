from rest_framework import serializers
from .models import Product , Image 
 
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image_url']

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

class ProductCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(write_only=True, required=False, allow_empty=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        # Extract image URLs from validated_data
        image_urls = validated_data.pop('images', [])

        # Check if data is a list of items
        if isinstance(validated_data, list):
            # Create a list to store the created products
            created_products = []

            # Iterate through each item in the list and create a Product
            for data in validated_data:
                # Create Product instance without images
                product = Product.objects.create(**data)
                # Create Image instances for each URL
                images = [Image.objects.create(image_url=image_url) for image_url in image_urls]
                # Add images to the product using set()
                product.images.set(images)
                created_products.append(product)

            return "Created successfully"
        else:
            # If it's not a list, create a single Product
            # Create Product instance without images
            product = Product.objects.create(**validated_data)

            # Create Image instances for each URL
            images = [Image.objects.create(image_url=image_url) for image_url in image_urls]

            # Add images to the product using set()
            product.images.set(images)

            return product
