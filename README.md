# Проект обзора фильмов
Проект представляет собой backend-приложение написанное на Python с использованием NoSQL БД Elasticsearch
и панели визуализации Kibana

## Как запустить проект:
* Склонировать текущий репозиторий: ```git clone git@github.com:topclassprogrammer/movie_review.git```
* Перейти в папку проекта: ```cd movie_review```
* В файле .env рекомендуется изменить пароль для переменной ELASTIC_PASSWORD
* Запустить контейнеры: ```docker-compose up -d```
* Через 30-40 секунд выполнить: 

```docker exec -it elasticsearch bash```

```bin/elasticsearch-reset-password -u kibana_system -i```

```y``` и дважды ввести пароль такой же который мы записали в переменную окружения ELASTIC_PASSWORD
* Чтобы открыть Kibana необходимо перейти по адресу http://localhost:5601 и аутентифицироваться 
под заданными переменными окружения ELASTIC_USERNAME и ELASTIC_PASSWORD
