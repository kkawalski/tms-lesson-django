from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from users.models import User
from users.api.serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
