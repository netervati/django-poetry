# DjangoPoetry
[DjangoPoetry](https://django-poetry.vercel.app/) is a public API that provides data of poems and poets for poetry enthusiasts. It follows the REST API structure and returns data in JSON format. It's easy to utilize and you can simply begin retrieving data using fetch, ajax, or axios without using any key or authentication.
<br />

## Technologies Used

|Purpose|Tool|
|:-----|:-----|
|Backend Structure|django, djangorestframework, django-cors-headers|
|Code Formatter|black|
|Scripts|python-fire|
|Type Checking|mypy, django-stubs, djangorestframework-stubs|
|Unit Testing|pytest, pytest-django, pytest-mock|
<br />

## Test Locally
1. Clone Repository:
```
$ git clone https://github.com/netervati/django-poetry.git
```
2. Start virtual environment (e.g. pipenv):
```
$ pipenv shell
```
3. Install packages from Pipfile:
```
$ pipenv sync
```
4. Setup .env file:
```
ALLOWED_HOST=127.0.0.1
DJANGO_DB=sqlite3
# DJANGO_DB=postgresql
DJANGO_DEBUG=true
DJANGO_SECRET_KEY=
# For postgresql db
POSTGRESQL_DB_HOST=
POSTGRESQL_DB_NAME=
POSTGRESQL_DB_PASS=
POSTGRESQL_DB_PORT=
POSTGRESQL_DB_USER=
```
5. Migrate database:
```
$ cd backend/core/
$ python manage.py migrate
```
6. Run server:
```
$ python manage.py runserver
```

Check the [documentation](https://django-poetry.vercel.app/) for more information.
<br />

## Contribution
For now, the Trello board is private. However, if you would like to contribute, feel free to submit an issue and also link a fork of this project if you made a fix. 

If changes were made in the backend, make sure that they are covered with unit tests. Then, run the following checks:

- Unit test results:
```
$ pytest
```
- Code format:
```
$ black ./
```
- Type checking:
```
$ mypy ./
```
