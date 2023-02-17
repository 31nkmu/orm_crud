from typing import List

from sqlalchemy import select, update
from sqlalchemy.orm import Session

from config.settings import engine


class RetrieveMixin:
    """
    Выводит один продукт по id
    """

    def retrieve(self, request: dict, *args, **kwargs) -> dict:
        with Session(engine) as session:
            id_ = request.get('id')
            stmt = select(self.model).where(self.model.id.in_([id_]))
            instance = list(session.scalars(stmt))[0]
            serializer = self.serializer_class()
            data = serializer.serialize(instance)
            return data


class UpdateMixin:
    """
    Обновляет один объект продукта
    """

    def update(self, request: dict, *args, **kwargs):
        with Session(engine) as session:
            id_ = request.get('id')
            data = request.get('data')
            serializer = self.serializer_class()
            serializer.update_fields(data)
            data = serializer.validate(data)
            check_data = {'id': id_, 'user_id': data.get('user_id')}
            serializer.check_is_owner(check_data)
            serializer.perform_update(id_=id_, data=data)
            return data


class DestroyMixin:
    """
    Удаляет продукт по id
    """

    def destroy(self, request: dict, *args, **kwargs):
        serializer = self.serializer_class()
        serializer.check_is_owner(request)
        with Session(engine) as session:
            instance = session.get(self.model, request.get('id'))
            session.delete(instance)
            session.commit()


class ListMixin:
    """
    Выводит список продуктов
    """

    def get_all(self, *args, **kwargs) -> List[dict]:
        with Session(engine) as session:
            serializer = self.serializer_class()
            data = []
            data_from_db = session.query(self.model).all()
            for one_data in data_from_db:
                data.append(serializer.serialize(one_data))
            return data


class CreateMixin:
    """
    Создает новый продукт
    """

    def create(self, request: dict, *args, **kwargs) -> dict:
        with Session(engine) as session:
            serializer = self.serializer_class()
            data = request.get('data')
            serializer.create_fields(data)
            data = serializer.validate(data)
            data = self.model(**data)
            session.add(data)
            session.commit()
            return serializer.serialize(data)
