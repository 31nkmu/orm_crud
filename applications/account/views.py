from applications.account.serializers import UserSerializer, ForgotPasswordSerializer
from config.generics import ListCreateView, RetrieveView
from config.mixins import UpdateMixin
from config.models import User


class UserView(ListCreateView, RetrieveView):
    model = User
    serializer_class = UserSerializer


# a = UserView()
# ret = a.retrieve({'id': 1})
# a.create({
#     'data': {
#         'email': 'admin@ad.com',
#         'password': '1234',
#         'password2': '1234',
#     }
# })
# print(a.list())


class ForgotPasswordView(UpdateMixin):
    model = User
    serializer_class = ForgotPasswordSerializer

#
# a = ForgotPasswordView()
# a.update({
#     'data': {
#         'email': 'admin@.com',
#         'password': '1',
#         'password2': '1'
#     }
# })
