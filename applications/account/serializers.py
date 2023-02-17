from sqlalchemy import update
from sqlalchemy.orm import Session

from config.models import User
from config.serializers import ModelSerializer
from config.settings import engine


class UserSerializer(ModelSerializer):
    fields = {
        'create': ['email', 'password', 'password2'],
        'update': ['email', 'password']
    }

    def serialize(*args, **kwargs):
        instance = args[-1]
        data = {
            'email': instance.email,
            'username': instance.username,
            'password': instance.password,
        }
        return data

    def validate(self, *args, **kwargs):
        instance = args[-1]
        email = instance.get('email')
        password = instance.get('password')
        password2 = instance.pop('password2')
        with Session(engine) as session:
            user = session.query(User).filter(User.email == email).first()
            if user:
                raise Exception('Такой юзер уже существует')
        if email.split('.')[-1] not in ['com', 'ru'] or email.count('@') != 1:
            raise Exception('Неправильно введен email')
        if password != password2:
            raise Exception('Пароли не совпадают')
        return instance


class ForgotPasswordSerializer(ModelSerializer):
    fields = {
        'update': ['password', 'email', 'password2']
    }

    def serialize(self, *args, **kwargs):
        instance = args[-1]
        data = {
            'email': instance.email,
            'password': instance.password,
        }
        return data

    def validate(self, *args, **kwargs):
        instance = args[-1]
        email = instance.get('email')
        password = instance.get('password')
        password2 = instance.pop('password2')
        if password != password2:
            raise Exception('Пароли не совпадают')
        with Session(engine) as session:
            user = session.query(User).filter(User.email == email).first()
            if not user:
                raise Exception('Нет такого юзера')
            user_id = user.id
            self.change_password(user_id=user_id, password=password)

    def perform_update(self, id_, data):
        pass

    @staticmethod
    def change_password(user_id, password):
        data = {'password': password}
        stmt = update(User).where(User.id == user_id).values(**data)
        with engine.begin() as conn:
            conn.execute(
                stmt, [data],
            )
