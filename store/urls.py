from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.ProductList.as_view()),
    path('product/<int:id>/', views.ProductDetail.as_view()),
    path('collections/', views.CollectionList.as_view()),
    path('collections/<int:id>/', views.CollectionDetail.as_view(), name='collection-detail')
]

    # path('product/', views.product_list),
    # path('product/<int:id>/', views.product_detail),
    # path('collection/<int:pk>/', views.collection_detail, name='collection-detail')