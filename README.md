# Каталог книг

Последняя версия версия,помещенная в Docker, работают фикстуры.

## Для Использования Docker необходимо сделать следующее:

### Настройка проекта


Команды выполняются внутри папки app:

```bash
python manage.py ruserver
```

#### Применение миграций:

```bash
python manage.py migrate
```
docker-compose exec app bash
#### Создание суперпользователя

```bash
python manage.py createsuperuser
```


Проект доступен по адресу http://127.0.0.1:8000
