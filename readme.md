### Программа "Сеть производства и продаж"

Это DRF-приложение представляет собой систему для учета звеньев в сети производства и продаж.


### Использование

1. Установите зависимости, выполнив `pip install -r requirements.txt`.
2. Примените миграции с помощью `python manage.py migrate`.
3. Запустите сервер разработки с помощью `python manage.py runserver`.
4. Перейдите по адресу `http://127.0.0.1:8000` для доступа к приложению.

### Примечание

- Для использования фильтрации по стране в `NodeListCreateView`, добавьте параметр `country` к URL, например, `http://127.0.0.1:8000/node/?country=Россия`.
