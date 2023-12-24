from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer


class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        # Получите данные пользователя из сериализатора
        user_data = serializer.validated_data

        # Создайте пользователя, установив пароль с использованием set_password
        user = User.objects.create(
            email=user_data['email'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            is_active=False
        )
        user.set_password(user_data['password'])
        user.save()

        return Response({'detail': 'Сотрудник успешно зарегистрирован.\n'
                                   'Сообщите об этом менеджеру, чтобы он активировал ваш аккаунт,'
                                   ' и вы смогли приступить к работе.'}, status=status.HTTP_201_CREATED)
