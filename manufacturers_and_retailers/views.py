from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from manufacturers_and_retailers.models import Node, Contacts
from manufacturers_and_retailers.pagination import NodePagination
from manufacturers_and_retailers.serializers import NodeListCreateSerializer, OneNodeSerializer, ContactsSerializer


class NodeView(RetrieveUpdateDestroyAPIView):
    queryset = Node.objects.all()
    serializer_class = OneNodeSerializer
    permission_classes = [IsAuthenticated]  # доступно только активным сотрудникам


class NodeListCreateView(ListCreateAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeListCreateSerializer
    pagination_class = NodePagination
    permission_classes = [IsAuthenticated]  # доступно только активным сотрудникам

    def get_queryset(self):
        queryset = Node.objects.all()
        # фильтрация по стране
        country = self.request.query_params.get('country', None)
        if country:
            queryset = queryset.filter(contacts__country=country)
        return queryset


class ContactsListCreateView(ListCreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticated]  # доступно только активным сотрудникам
