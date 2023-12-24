from django.urls import path

from manufacturers_and_retailers.views import NodeListCreateView, NodeView, ContactsListCreateView

app_name = 'manufacturers_and_retailers'

urlpatterns = [
    path('node/', NodeListCreateView.as_view(), name='node'),
    path('node/<int:pk>/', NodeView.as_view(), name='node_id'),
    path('contact/', ContactsListCreateView.as_view(), name='contact'),
]
