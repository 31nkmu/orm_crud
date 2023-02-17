from sqlalchemy.orm import Session

from config.models import Product, Category
from config.serializers import ModelSerializer
from config.settings import engine


class ProductSerializer(ModelSerializer):
    fields = {
        'create': ['title', 'price', 'category_id', 'user_id'],
        'update': ['title', 'price', 'category_id']
    }
    model = Product

    def serialize(*args, **kwargs) -> dict:
        instance = args[-1]
        data = {
            'id': instance.id,
            'title': instance.title,
            'price': float(instance.price),
            'category': instance.category,
            'user': instance.user
        }
        return data

    @staticmethod
    def validate(*args, **kwargs):
        instance = args[-1]
        if len(instance.get('title')) > 60:
            raise Exception('Название продукта должно быть менее 60 букв')
        price = instance.get('price')
        if not type(price) in [int, float]:
            raise Exception('В качестве цены введите число')
        with Session(engine) as session:
            if not session.get(Category, instance['category_id']):
                raise Exception('Нет такой категории')
        return instance

    def check_is_owner(self, *args, **kwargs):
        instance = args[-1]
        id_ = instance.get('id')
        user_id = instance.get('user_id')
        with Session(engine) as session:
            product = session.get(self.model, id_)
            if product.user_id != user_id:
                raise Exception('Вы не являелетесь владельцем этого продукта')


class CategorySerializer(ModelSerializer):
    model = Category
    fields = {
        'create': ['title'],
        'update': ['title']
    }

    def serialize(*args, **kwargs):
        instance = args[-1]
        data = {
            'title': instance.title,
            'id': instance.id
        }
        return data

    def validate(*args, **kwargs):
        instance = args[-1]
        title = instance.get('title')
        if len(instance.get('title')) > 60:
            raise Exception('Название продукта должно быть менее 60 букв')
        with Session(engine) as session:
            category = session.query(Category).filter(Category.title == title).first()
            if category:
                raise Exception('Такая категория уже существует')
        return instance
