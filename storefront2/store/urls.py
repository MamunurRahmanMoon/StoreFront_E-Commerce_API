from django.urls import path

# from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views
from pprint import pprint

router = routers.DefaultRouter()
router.register("products", views.ProductViewSet, basename="products")
router.register("collections", views.CollectionViewSet)
router.register("carts", views.CartViewSet)
router.register("customers", views.CustomerViewSet)

##### Nested Router for Product Review

# https://github.com/alanjds/drf-nested-routers
# pip install drf-nested-routers

product_router = routers.NestedDefaultRouter(router, "products", lookup="product")
product_router.register("reviews", views.ReviewViewSet, basename="product-review")

##### Nested Router for Product Review
item_router = routers.NestedDefaultRouter(router, "carts", lookup="cart")
item_router.register("items", views.CartItemViewSet, basename="cart-items-details")

#### URLConf
urlpatterns = router.urls + product_router.urls + item_router.urls


# urlpatterns = [
#     # path("products/", views.ProductList.as_view()),
#     # path("products/<int:pk>/", views.ProductDetails.as_view()),
#     # path("collection/", views.CollectionList.as_view()),
#     # path("collection/<int:pk>", views.CollectionDetails.as_view(), name="collection_details")
# ]
