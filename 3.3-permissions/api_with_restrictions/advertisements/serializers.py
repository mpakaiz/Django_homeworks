from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )
        read_only_fields = ['creator', ]
    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        print(f'status from data: {self.initial_data.get("status")}')
        user = self.context['request'].user
        count = len(self.context['view'].queryset.filter(status='OPEN', creator=user))
        print(f'всего открытых объявлений: {count}')
        print(f'1: {"OPEN" == self.initial_data.get("status")}')
        print(f'2: {None == self.initial_data.get("status")}')
        print(f'3: {count >= 10}')
        if 'OPEN' == self.initial_data.get('status') and count >= 10 or None == self.initial_data.get('status') and count >= 10:
            raise ValidationError('Слишком много открытых записей')
        return data
