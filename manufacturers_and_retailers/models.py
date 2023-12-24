from django.db import models

from manufacturers_and_retailers.utils import check_nesting_depth


class Contacts(models.Model):
    """
    Контакты звена в сети
    """
    email = models.EmailField(verbose_name='Почта', unique=True)
    country = models.CharField(max_length=50, default='Россия', verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')

    def __str__(self):
        return f'{self.country} {self.city} {self.street} {self.house_number} - {self.email}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Node(models.Model):
    """
    Модель для звена в сети
    """
    KIND_CHOICES = [
        ('factory', 'Завод'),
        ('retail_network', 'Розничная сеть'),
        ('individual_entrepreneur', 'Индивидуальный предприниматель'),
    ]
    name = models.CharField(max_length=255, verbose_name='Имя', unique=True)
    kind_of_node = models.CharField(max_length=25, choices=KIND_CHOICES, verbose_name='Тип звена')
    node_level = models.IntegerField(blank=True, verbose_name='Уровень звена')
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE, verbose_name='Контакты')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    debt = models.IntegerField(default=0, verbose_name='Долг перед поставщиком')
    supplier = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Поставщик')

    def save(self, *args, **kwargs):
        self.node_level = check_nesting_depth(self)
        super(Node, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Звено'
        verbose_name_plural = 'Звенья сети'


class Product(models.Model):
    """
    Продукт
    """
    name = models.CharField(max_length=128, verbose_name='Название', unique=True)
    model = models.CharField(max_length=64, verbose_name='Модель')
    created_at = models.DateTimeField(verbose_name='Дата выхода на рынок')
    node = models.ForeignKey(Node, on_delete=models.CASCADE, verbose_name='Звено')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
