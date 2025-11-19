from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Product, Collection, OrderItem
from .serializers import ProductSerializer

# Create your views here.
@api_view()
def product_list(request):
    query_set = Product.objects.select_related('collection').all()
    serializer = ProductSerializer(query_set, many=True, context={'request': request})
    return Response(serializer.data)

@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    print(serializer.data)
    return Response(serializer.data)

@api_view()
def collection_detail(request, pk):
    return Response(pk)
    















# class ProductViewSet(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get_serializer_context(self):
#         return {'request': self.request}
    
#     def destroy(self, request, *args, **kwargs):
#         if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
#             return Response({'error': 'Product cannot be deleted since it is related to an order'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         return super().destroy(request, *args, **kwargs)
     
 
# class CollectionViewSet(ModelViewSet):
#     queryset = Collection.objects.annotate(products_count=Count('product')).all()
#     serializer_class = CollectionSerializer 

#     def destroy(self, request, *args, **kwargs):
#         if Product.objects.filter(collection_id=kwargs['pk']).count() > 0:
#             return Response({'error': 'Collection cannot be deleted since it has products'})
#         return super().destroy(request, *args, **kwargs)

    # def get(self, request):
    #     collection = Collection.objects.all()
    #     serializer = CollectionSerializer(collection, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def post(self, request):
    #     serializer = CollectionSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    
   





# @api_view(['GET', 'POST'])
# def product_list(request):
#     if request.method == 'GET':
#         query_set = Product.objects.select_related('collection').all()
#         serializer = ProductSerializer(query_set, many=True, context={'request': request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         # serializer.validated_data
#         serializer.save()
#         return Response('ok')
            

# @api_view()
# def product_detail(request, id):
#     product = get_list_or_404(Product, pk=id)
#     serializer = ProductSerializer(product)
#     return Response(serializer.data)

# @api_view()
# def collection_detail(request, pk):
#     return Response('ok')
    