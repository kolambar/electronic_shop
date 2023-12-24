from rest_framework import serializers

from manufacturers_and_retailers.models import Node, Contacts, Product


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        exclude = ('node_level', 'debt', )


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
