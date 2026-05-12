---
title: Расширенное использование middleware
source: https://fastapi.tiangolo.com/ru/advanced/middleware/
---

# Расширенное использование middleware

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/advanced/middleware/)

В основном руководстве вы читали, как добавить [пользовательское middleware](https://fastapi.tiangolo.com/ru/tutorial/middleware/) ([local](./../06_учебник-руководство-пользователя/32_middleware-промежуточный-слой.md)) в ваше приложение.

А затем — как работать с [CORS с помощью `CORSMiddleware`](https://fastapi.tiangolo.com/ru/tutorial/cors/) ([local](./../06_учебник-руководство-пользователя/33_cors-cross-origin-resource-sharing.md)).

В этом разделе посмотрим, как использовать другие middleware.

## Добавление ASGI middleware

Так как **FastAPI** основан на Starlette и реализует спецификацию ASGI, вы можете использовать любое ASGI middleware.

Middleware не обязательно должно быть сделано специально для FastAPI или Starlette — достаточно, чтобы оно соответствовало спецификации ASGI.

В общем случае ASGI middleware — это классы, которые ожидают получить ASGI‑приложение первым аргументом.

Поэтому в документации к сторонним ASGI middleware, скорее всего, вы увидите что‑то вроде:

```
 
    from unicorn import UnicornMiddleware
    
    app = SomeASGIApp()
    
    new_app = UnicornMiddleware(app, some_config="rainbow")
    

```

Но FastAPI (точнее, Starlette) предоставляет более простой способ, который гарантирует корректную обработку внутренних ошибок сервера и корректную работу пользовательских обработчиков исключений.

Для этого используйте `app.add_middleware()` (как в примере с CORS).

```
 
    from fastapi import FastAPI
    from unicorn import UnicornMiddleware
    
    app = FastAPI()
    
    app.add_middleware(UnicornMiddleware, some_config="rainbow")
    

```

`app.add_middleware()` принимает класс middleware в качестве первого аргумента и любые дополнительные аргументы, которые будут переданы этому middleware.

## Встроенные middleware

**FastAPI** включает несколько middleware для распространённых сценариев. Ниже рассмотрим, как их использовать.

Технические детали

В следующих примерах вы также можете использовать `from starlette.middleware.something import SomethingMiddleware`.

**FastAPI** предоставляет несколько middleware в `fastapi.middleware` для удобства разработчика. Но большинство доступных middleware приходит напрямую из Starlette.

## `HTTPSRedirectMiddleware`

Гарантирует, что все входящие запросы должны использовать либо `https`, либо `wss`.

Любой входящий запрос по `http` или `ws` будет перенаправлен на безопасную схему.

Python 3.10+

```
 
    from fastapi import FastAPI
    from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
    
    app = FastAPI()
    
    app.add_middleware(HTTPSRedirectMiddleware)
    
    
    @app.get("/")
    async def main():
        return {"message": "Hello World"}
    

```

## `TrustedHostMiddleware`

Гарантирует, что во всех входящих запросах корректно установлен `Host`‑заголовок, чтобы защититься от атак на HTTP‑заголовок Host.

Python 3.10+

```
 
    from fastapi import FastAPI
    from fastapi.middleware.trustedhost import TrustedHostMiddleware
    
    app = FastAPI()
    
    app.add_middleware(
        TrustedHostMiddleware, allowed_hosts=["example.com", "*.example.com"]
    )
    
    
    @app.get("/")
    async def main():
        return {"message": "Hello World"}
    

```

Поддерживаются следующие аргументы:

  * `allowed_hosts` — список доменных имён, которые следует разрешить как имена хостов. Подстановки вида `*.example.com` поддерживаются для сопоставления поддоменов. Чтобы разрешить любой хост, используйте либо `allowed_hosts=["*"]`, либо не добавляйте это middleware.
  * `www_redirect` — если установлено в True, запросы к не‑www версиям разрешённых хостов будут перенаправляться на их www‑аналоги. По умолчанию — `True`.

Если входящий запрос не проходит валидацию, будет отправлен ответ `400`.

## `GZipMiddleware`

Обрабатывает GZip‑ответы для любых запросов, которые включают `"gzip"` в заголовке `Accept-Encoding`.

Это middleware обрабатывает как обычные, так и потоковые ответы.

Python 3.10+

```
 
    from fastapi import FastAPI
    from fastapi.middleware.gzip import GZipMiddleware
    
    app = FastAPI()
    
    app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=5)
    
    
    @app.get("/")
    async def main():
        return "somebigcontent"
    

```

Поддерживаются следующие аргументы:

  * `minimum_size` — не сжимать GZip‑ом ответы, размер которых меньше этого минимального значения в байтах. По умолчанию — `500`.
  * `compresslevel` — уровень GZip‑сжатия. Целое число от 1 до 9. По умолчанию — `9`. Более низкое значение — быстрее сжатие, но больший размер файла; более высокое значение — более медленное сжатие, но меньший размер файла.

## Другие middleware

Существует много других ASGI middleware.

Например:

  * [`ProxyHeadersMiddleware` от Uvicorn](https://github.com/encode/uvicorn/blob/master/uvicorn/middleware/proxy_headers.py)
  * [MessagePack](https://github.com/florimondmanca/msgpack-asgi)

Чтобы увидеть другие доступные middleware, посмотрите [документацию по middleware в Starlette](https://www.starlette.dev/middleware/) и [список ASGI Awesome](https://github.com/florimondmanca/awesome-asgi).
  *[ASGI]: Asynchronous Server Gateway Interface – Асинхронный шлюзовой интерфейс сервера
