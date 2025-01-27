# Montechelo TO-DO API

## Help

### Run Start

#### Start dev
```shell
docker compose build && docker compose up
```

#### Start Production
```shell
sh deploy
```

### Migrations

#### Run makemigrations
```shell
docker compose run --rm montechelo python manage.py makemigrations
```

#### Run migrate
```shell
docker compose run --rm montechelo python manage.py migrate
```

#### Create trigger
docker compose run --rm montechelo python manage.py makemigrations --empty trigger --name update_number_of_questions_in_assessment

### Dumpdata and loaddata


#### Run Dumpdata
```shell
docker compose run --rm montechelo python  manage.py dumpdata user --indent 2 > user.json
```

#### Run Loaddata
```shell
docker compose run --rm montechelo python manage.py loaddata user.json
```

### APP

#### Run startapp
```shell
docker compose run --rm montechelo python manage.py startapp nameApp
```
