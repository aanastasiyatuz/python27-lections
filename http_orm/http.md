# Protocols
> **HTTP** - Hyper Text Trasfer Protocol. Протокол, который построен на протоколах **TCP/IP**.

> **HTTPS** - более новая версия HTTP, где появилось шифрование и SSL сертификаты

## HTTP methods
* **GET** - получение данных
* **POST** - отправка данных на создание
* **PUT** - полное обновление или создание
* **PATCH** - частичное обновление
* **DELETE** - удаление
* TRACE - трассировка (проверка связи)
* HEAD - получение headers для запроса
* OPTIONS - получение списка методов на данную url

# Status Code
* 1XX - информационные
* 2XX - успешные
* 3XX - перенаправление
* 4XX - ошибки клиента
* 5XX - ошибки сервера

# URL
> Uniform resource locator `https://www.google.com/search?q=hello`

> **DOMAIN** - уникальное название к которому прикреплен определенный сервер (ip address) `www.google.com`

> **URI** - подпуть `/search`

> **Query Params** - пары ключ=значение, идут после ? `q=hello`
