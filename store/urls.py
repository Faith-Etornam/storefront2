from rest_framework_nested import routers 
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='product')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-review')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')


urlpatterns = router.urls + products_router.urls + carts_router.urls


# urlpatterns = [
#     # path('products/', views.ProductList.as_view()),
#     # path('products/<int:id>/', views.ProductDetail.as_view()),
#     # path('collections/', views.CollectionList.as_view()),
#     # path('collections/<int:id>/', views.CollectionDetail.as_view(), name='collection-detail')
# ]


# router = SimpleRouter()
# router.register('products', views.ProductViewSet)
# router.register('collections', views.CollectionViewSet)


# urlpatterns = [

#     path('', include(router.urls))
#     # path('product/', views.ProductList.as_view()),
#     # path('product/<int:pk>/', views.ProductDetail.as_view()),
#     # path('collections/', views.CollectionList.as_view()),
#     # path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail')
# ]

    # path('product/', views.product_list),
    # path('product/<int:id>/', views.product_detail),
    # path('collection/<int:pk>/', views.collection_detail, name='collection-detail')