# wb_parser
Парсер для сайта Widlberries.  
Имеются 4 конечные точки:
- Добавить номенклатуру: пользователь указывает nm_id, сервис парсит данные с сайта www.wildberries.ru и сохраняет их в базу данных PostgreSQL
- Получить товар по номенклатуре
- Получить все товары
- Удалить товар по номенклатуре

Карточка товара в базе содержит следующие поля:
- nm_id
- name
- brand
- brand_id
- site_brand_id
- supplier_id
- sale
- price
- sale_price
- rating
- feedbacks
- colors

## Технологии
Python 3.10, FastAPI, SQLAlchemy, requests, Pydantic, Alembic, Docker, PostgreSQL

## Локальный запуск проекта
Для запуска подойдёт Docker 20.10.21, Docker Compose 2.12.2.  
Клонируйте репозиторий:
```
git clone git@github.com:ElenaChuvasheva/wb_parser.git
```
Перейдите в папку wb_parser/:
```
cd wb_parser\
```
Создайте в этой папке файл .env с переменными окружения для работы с базой данных, значения имени пользователя и пароля даны для примера:
```
DB_NAME=parser_db
DB_USER=root
DB_PASS=root
DB_HOST=db
DB_PORT=5432
POSTGRES_USER=root
POSTGRES_DB=parser_db
POSTGRES_PASSWORD=root
```
В этой же папке запустите команду сборки контейнеров:
```
docker-compose up
```
Запустите миграции:
```
docker-compose exec web alembic upgrade head
```
Проект откроется по адресу http://127.0.0.1:8000/ 

## Примеры запросов
GET /items/ - получение всех товаров  
POST /items/ - добавление товара по номенклатуре. Тело запроса:
```
{
    "nm_id": 139760729
}
```
GET /items/139760729/ - получение карточки товара по номенклатуре  
DELETE /items/139760729/ - удаление карточки товара по номенклатуре
