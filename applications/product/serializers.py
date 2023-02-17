from sqlalchemy.orm import Session

from config.models import Product
from config.serializers import ModelSerializer
from config.settings import engine


class ProductSerializer(ModelSerializer):
    fields = {
        'create': ['title', 'price', 'category_id', 'user_id'],
        'update': ['title', 'price', 'category_id']
    }

    def serialize(*args, **kwargs) -> dict:
        instance = args[-1]
        data = {
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
            if not session.get(Product, instance['category_id']):
                raise Exception('Нет такой категории')
        return instance


class CategorySerializer(ModelSerializer):
    fields = {
        'create': ['title'],
        'update': ['title']
    }

    def serialize(*args, **kwargs):
        instance = args[-1]
        data = {
            'title': instance.title
        }
        return data

    def validate(*args, **kwargs):
        instance = args[-1]
        if len(instance.get('title')) > 60:
            raise Exception('Название продукта должно быть менее 60 букв')
