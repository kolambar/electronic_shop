from rest_framework import serializers

from manufacturers_and_retailers.models import Node, Contacts, Product


class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class NodeListCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для списка звеньев сети и для их создания. При создании достаточно указать id контактов
    """
    contacts = serializers.PrimaryKeyRelatedField(queryset=Contacts.objects.all(), many=False)

    class Meta:
        model = Node
        fields = '__all__'
        read_only_fields = ('node_level', 'debt', 'created_at', )  # поля, которые не получится редактировать


class OneNodeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для одного звена сети, его просмотра, обновления и удаления.
    Выводит полную информацию о контактах и продуктах. Позволяет редактировать контакты.
    """
    contacts = ContactsSerializer(required=False)  # можно не присваивать
    products = ProductSerializer(source='product_set', many=True, read_only=True)

    def update(self, instance, validated_data):
        """
        Обновляет контакты помимо обычных функций
        :param instance:
        :param validated_data:
        :return:
        """
        contacts_data = validated_data.pop('contacts', None)
        if contacts_data:
            contacts_instance = instance.contacts
            ContactsSerializer().update(contacts_instance, contacts_data)

        return instance

    class Meta:
        model = Node
        fields = '__all__'
        read_only_fields = ('node_level', 'debt', 'created_at', )  # поля, которые не получится редактировать
