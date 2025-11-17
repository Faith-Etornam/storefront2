from .models import Product, Collection
from rest_framework import serializers
from decimal import Decimal

class CollectionSerializer(serializers.ModelSerializer):
    
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    def get_products_count(self, collection: Collection):
        return collection.product_set.count()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'collection', 'price_with_tax', 'inventory']
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     view_name='collection-detail'
    # )
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=8, decimal_places=2, source='unit_price')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)

# class CollectionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Collection
#         fields = ['id', 'title']

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['id', 'title', 'unit_price', 'collection']
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # unit_price = serializers.DecimalField(max_digits=8, decimal_places=2)
    # collection = serializers.HyperlinkedRelatedField(
    #     queryset = Collection.objects.all(),
    #     view_name = 'collection-detail'
    # )
