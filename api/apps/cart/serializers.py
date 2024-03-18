from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Cart
        fields = "__all__"
        
    def get_user(self, obj):
        request = self.context.get('request')
        return request.user

class CartGetSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = [ "id" , "product" , "quantity" ]
        
    def get_product(self, obj):
        product = {
            'id': obj.product.id,
            'title': obj.product.title,
            'price': obj.product.price,
            'discount': obj.product.discountPercentage,
            'thumbnail': obj.product.thumbnail,
            }
        return product