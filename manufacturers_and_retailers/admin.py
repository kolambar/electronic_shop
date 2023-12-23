from django.contrib import admin
from rest_framework.reverse import reverse

from manufacturers_and_retailers.models import Node, Contacts, Product


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    readonly_fields = ('node_level', )
    list_display = ('name', 'kind_of_node', 'node_level', 'contacts', 'created_at', 'debt', 'supplier', )
    list_filter = ('kind_of_node', 'node_level', )
    search_fields = ('name', )

    # def supplier_link(self, obj):
    #     # Ваша логика для получения ссылки на поставщика
    #     if obj.supplier:
    #         return f'<a href="{reverse("admin:manufacturers_and_retailers_node_change", args=[obj.supplier.id])}">{obj.supplier.name}</a>'
    #     return 'No Supplier'
    #
    # supplier_link.allow_tags = True
    # supplier_link.short_description = 'Поставщик'


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number', )
    list_filter = ('country', 'city', )
    search_fields = ('email', 'country', 'city', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'created_at', 'node', )
    list_filter = ('node', )
    search_fields = ('name', )
