from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Cart
        fields = '__all__'

    def get_user(self, obj):
        request = self.context.get('request')
        return request.user