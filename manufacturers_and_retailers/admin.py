from django.contrib import admin

from manufacturers_and_retailers.models import Node, Contacts, Product


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1  # Количество дополнительных форм для отображения


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    """
    Отображение модели звена
    """
    readonly_fields = ('node_level', )

    inlines = [ProductInline]  # Добавляем вложенные продукты
    list_display = ('name', 'kind_of_node', 'node_level', 'contacts', 'created_at', 'debt', 'supplier', )
    list_filter = ('kind_of_node', 'node_level', 'contacts__country', 'contacts__city', )
    search_fields = ('name', )

    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        # Обновление всех выбранных объектов, устанавливая задолженность в 0
        queryset.update(debt=0)

    clear_debt.short_description = "Очистить задолженность"


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    """
    Отображение модели контактов
    """
    list_display = ('email', 'country', 'city', 'street', 'house_number', )
    list_filter = ('country', 'city', )
    search_fields = ('email', 'country', 'city', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Отображение модели продуктов
    """
    list_display = ('name', 'model', 'created_at', 'node', )
    list_filter = ('node', )
    search_fields = ('name', )
