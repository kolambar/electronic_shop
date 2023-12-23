from rest_framework import serializers

from manufacturers_and_retailers.models import Node


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        exclude = ['node_level']
