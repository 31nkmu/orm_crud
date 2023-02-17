from abc import ABC, abstractmethod

from sqlalchemy import update

from config.settings import engine


class ModelSerializer(ABC):
    @abstractmethod
    def serialize(self, *args, **kwargs):
        pass

    @abstractmethod
    def validate(self, *args, **kwargs):
        pass

    @staticmethod
    def _validate_fields(fields, instance):
        for field in fields:
            if not instance.get(field):
                raise Exception(f'Нужно ввести обязательное поле {field}')

    def update_fields(self, *args, **kwargs):
        instance = args[-1]
        fields = self.fields['update']
        self._validate_fields(fields=fields, instance=instance)

    def create_fields(self, *args, **kwargs):
        instance = args[-1]
        fields = self.fields['create']
        self._validate_fields(fields=fields, instance=instance)

    def perform_update(self, id_, data):
        stmt = update(self.model).where(self.model.id == id_).values(**data)
        with engine.begin() as conn:
            conn.execute(
                stmt, [data],
            )
