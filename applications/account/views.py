from applications.account.serializers import UserSerializer, ForgotPasswordSerializer, LoginSerializer
from config.generics import ListCreateView, RetrieveView
from config.mixins import UpdateMixin
from config.models import User


class UserView(ListCreateView, RetrieveView):
    model = User
    serializer_class = UserSerializer


class LoginView(RetrieveView):
    model = User
    serializer_class = LoginSerializer

    def get(self, request, *args, **kwargs):
        data = request.get('data')
        serializer = self.serializer_class()
        data = serializer.validate(data)
        return data


class ForgotPasswordView(UpdateMixin):
    model = User
    serializer_class = ForgotPasswordSerializer
