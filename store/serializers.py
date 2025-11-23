from rest_framework import serializers
from decimal import Decimal
from .models import Collection, Product, Review, Cart, CartItem

class CollectionSerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'inventory', 'unit_price', 'price_with_tax', 'collection']
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    
    def calculate_tax(self, product):
        return product.unit_price * Decimal(1.1)
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'user_name', 'description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data) 
    
class CartItemProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price']
    
class CartItemSerializer(serializers.ModelSerializer):

    product = CartItemProductSerializer()
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart):
        return sum([item.product.unit_price * item.quantity for item in cart.items.all()])
    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price']

class AddCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity']
















# from .models import Product, Collection
# from rest_framework import serializers
# from decimal import Decimal

# class CollectionSerializer(serializers.ModelSerializer):
#     products_count = serializers.IntegerField()

#     class Meta:
#         model = Collection
#         fields = ['id', 'title', 'products_count']


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['id', 'title', 'unit_price', 'collection', 'price_with_tax', 'inventory']
#     price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    
#     def calculate_tax(self, product: Product):
#         return product.unit_price * Decimal(1.1)
    
#     # collection = serializers.HyperlinkedRelatedField(
#     #     queryset=Collection.objects.all(),
#     #     view_name='collection-detail'
#     # )
#     # id = serializers.IntegerField()
#     # title = serializers.CharField(max_length=255)
#     # price = serializers.DecimalField(max_digits=8, decimal_places=2, source='unit_price')


# # class CollectionSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Collection
# #         fields = ['id', 'title']

# # class ProductSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Product
# #         fields = ['id', 'title', 'unit_price', 'collection']
#     # id = serializers.IntegerField()
#     # title = serializers.CharField(max_length=255)
#     # unit_price = serializers.DecimalField(max_digits=8, decimal_places=2)
#     # collection = serializers.HyperlinkedRelatedField(
#     #     queryset = Collection.objects.all(),
#     #     view_name = 'collection-detail'
#     # )