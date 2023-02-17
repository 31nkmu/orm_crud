from config.mixins import RetrieveMixin, ListMixin, CreateMixin, UpdateMixin, DestroyMixin


class RetrieveUpdateDestroyView(RetrieveMixin, UpdateMixin, DestroyMixin):
    """
    Удаляет, обновляет, выводит один объект по id
    """

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ListCreateView(ListMixin, CreateMixin):
    """
    Выводит список всех объектов, создает объект
    """

    def list(self, *args, **kwargs):
        return self.get_all(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RetrieveView(RetrieveMixin):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ModelView(RetrieveUpdateDestroyView, ListCreateView):
    pass
