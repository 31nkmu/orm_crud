from applications.product.serializers import ProductSerializer, CategorySerializer
from config.generics import ModelView
from config.models import Product, Category


class ProductView(ModelView):
    model = Product
    serializer_class = ProductSerializer


class CategoryView(ModelView):
    model = Category
    serializer_class = CategorySerializer


product = ProductView()
# a = product.retrieve({'id': 1})
# print(a)
# category = CategoryView()
# b = category.retrieve({'id': 1})
# print(b)
# product.create({
#     'data': {
#         'title': 'test3',
#         'price': 999,
#         'category_id': 1,
#         'user_id': 1
#     }
# })
# product.update({
#     'id': 1,
#     'data': {
#         'title': 'test_update',
#         'price': 11111,
#         'category_id': 1,
#     }
# })

category = CategoryView()
# category.create({'data': {'title': 'category12'}})
# category.update({
#     'id': 1,
#     'data': {
#         'title': 'category12'
#     }
# })
print(category.list())
print(category.get({'id': 1}))
category.delete({'id': 2})
