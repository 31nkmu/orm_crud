from applications.product.serializers import ProductSerializer, CategorySerializer
from config.generics import ModelView
from config.models import Product, Category


class ProductView(ModelView):
    model = Product
    serializer_class = ProductSerializer


class CategoryView(ModelView):
    model = Category
    serializer_class = CategorySerializer
