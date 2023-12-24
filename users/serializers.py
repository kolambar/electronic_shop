from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            raise serializers.ValidationError("Пароли не совпадают.")

        return data

    def create(self, validated_data):
        validated_data.pop('password2', None)
        return super().create(validated_data)
