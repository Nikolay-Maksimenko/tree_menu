## Tree menu

Django app, реализующий древовидное меню, соблюдая следующие условия:

1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД
 
При выполнении задания из библиотек использовались только Django и стандартные библиотеки Python.

## Инструкции по запуску

1. Создайте виртуальное окружение: `python3 -m venv env`
2. Активируйте виртуальное окружение: 
   - windows: `env/bin/acticate`
   - ubuntu: `source env/bin/activate`
3. Установите все зависимости: `pip install -r requirements.txt`
4. Выполните миграции: `python manage.py migrate`
5. Запустите сервер: `python manage.py runserver`
6. Создайте суперпользователя: `python manage.py createsuperuser`
7. Для перехода в административную панель: `http://127.0.0.1:8000/admin/`
8. Для перехода в меню: `http://127.0.0.1:8000/tree_menu/`

## Инструкции по запуску в docker:
1. Создание образа проекта:`sudo docker build -t phonebook .`
2. Запуск контейнера: `docker run --rm --name tree_menu -p 8080:8080 tree`
3. Создание суперпользователя: `docker exec -it tree_menu python manage.py createsuperuser`
4. Для перехода в административную панель: `http://127.0.0.1:8080/admin/`
5. Для перехода в меню: `http://127.0.0.1:8080/tree_menu/`
