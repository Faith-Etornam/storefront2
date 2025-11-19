from django.urls import include, path
from rest_framework .routers import SimpleRouter
from . import views


urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail),
    path('collections/<int:pk>/', views.collection_detail, name='collection-detail'),
   
]


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