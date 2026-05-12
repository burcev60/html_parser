---
title: Пользовательские классы Request и APIRoute
source: https://fastapi.tiangolo.com/ru/how-to/custom-request-and-route/
---

# Пользовательские классы Request и APIRoute

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/how-to/custom-request-and-route/)

В некоторых случаях может понадобиться переопределить логику, используемую классами `Request` и `APIRoute`.

В частности, это может быть хорошей альтернативой логике в middleware.

Например, если вы хотите прочитать или изменить тело запроса до того, как оно будет обработано вашим приложением.

Опасность

Это «продвинутая» возможность.

Если вы только начинаете работать с **FastAPI** , возможно, стоит пропустить этот раздел.

## Сценарии использования

Некоторые сценарии:

  * Преобразование тел запросов, не в формате JSON, в JSON (например, [`msgpack`](https://msgpack.org/index.html)).
  * Распаковка тел запросов, сжатых с помощью gzip.
  * Автоматическое логирование всех тел запросов.

## Обработка пользовательского кодирования тела запроса

Посмотрим как использовать пользовательский подкласс `Request` для распаковки gzip-запросов.

И подкласс `APIRoute`, чтобы использовать этот пользовательский класс запроса.

### Создать пользовательский класс `GzipRequest`

Совет

Это учебный пример, демонстрирующий принцип работы. Если вам нужна поддержка Gzip, вы можете использовать готовый [`GzipMiddleware`](https://fastapi.tiangolo.com/ru/advanced/middleware/#gzipmiddleware) ([local](./../08_расширенное-руководство-пользователя/15_расширенное-использование-middleware.md#gzipmiddleware)).

Сначала создадим класс `GzipRequest`, который переопределит метод `Request.body()` и распакует тело запроса при наличии соответствующего HTTP-заголовка.

Если в заголовке нет `gzip`, он не будет пытаться распаковывать тело.

Таким образом, один и тот же класс маршрута сможет обрабатывать как gzip-сжатые, так и несжатые запросы.

Python 3.10+

```
 
    import gzip
    from collections.abc import Callable
    from typing import Annotated
    
    from fastapi import Body, FastAPI, Request, Response
    from fastapi.routing import APIRoute
    
    
    class GzipRequest(Request):
        async def body(self) -> bytes:
            if not hasattr(self, "_body"):
                body = await super().body()
                if "gzip" in self.headers.getlist("Content-Encoding"):
                    body = gzip.decompress(body)
                self._body = body
            return self._body
    
    
    class GzipRoute(APIRoute):
        def get_route_handler(self) -> Callable:
            original_route_handler = super().get_route_handler()
    
            async def custom_route_handler(request: Request) -> Response:
                request = GzipRequest(request.scope, request.receive)
                return await original_route_handler(request)
    
            return custom_route_handler
    
    
    app = FastAPI()
    app.router.route_class = GzipRoute
    
    
    @app.post("/sum")
    async def sum_numbers(numbers: Annotated[list[int], Body()]):
        return {"sum": sum(numbers)}
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    import gzip
    from collections.abc import Callable
    
    from fastapi import Body, FastAPI, Request, Response
    from fastapi.routing import APIRoute
    
    
    class GzipRequest(Request):
        async def body(self) -> bytes:
            if not hasattr(self, "_body"):
                body = await super().body()
                if "gzip" in self.headers.getlist("Content-Encoding"):
                    body = gzip.decompress(body)
                self._body = body
            return self._body
    
    
    class GzipRoute(APIRoute):
        def get_route_handler(self) -> Callable:
            original_route_handler = super().get_route_handler()
    
            async def custom_route_handler(request: Request) -> Response:
                request = GzipRequest(request.scope, request.receive)
                return await original_route_handler(request)
    
            return custom_route_handler
    
    
    app = FastAPI()
    app.router.route_class = GzipRoute
    
    
    @app.post("/sum")
    async def sum_numbers(numbers: list[int] = Body()):
        return {"sum": sum(numbers)}
    

```

### Создать пользовательский класс `GzipRoute`

Далее создадим пользовательский подкласс `fastapi.routing.APIRoute`, который будет использовать `GzipRequest`.

На этот раз он переопределит метод `APIRoute.get_route_handler()`.

Этот метод возвращает функцию. Именно эта функция получает HTTP-запрос и возвращает HTTP-ответ.

Здесь мы используем её, чтобы создать `GzipRequest` из исходного HTTP-запроса.

Python 3.10+

```
 
    import gzip
    from collections.abc import Callable
    from typing import Annotated
    
    from fastapi import Body, FastAPI, Request, Response
    from fastapi.routing import APIRoute
    
    
    class GzipRequest(Request):
        async def body(self) -> bytes:
            if not hasattr(self, "_body"):
                body = await super().body()
                if "gzip" in self.headers.getlist("Content-Encoding"):
                    body = gzip.decompress(body)
                self._body = body
            return self._body
    
    
    class GzipRoute(APIRoute):
        def get_route_handler(self) -> Callable:
            original_route_handler = super().get_route_handler()
    
            async def custom_route_handler(request: Request) -> Response:
                request = GzipRequest(request.scope, request.receive)
                return await original_route_handler(request)
    
            return custom_route_handler
    
    
    app = FastAPI()
    app.router.route_class = GzipRoute
    
    
    @app.post("/sum")
    async def sum_numbers(numbers: Annotated[list[int], Body()]):
        return {"sum": sum(numbers)}
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    import gzip
    from collections.abc import Callable
    
    from fastapi import Body, FastAPI, Request, Response
    from fastapi.routing import APIRoute
    
    
    class GzipRequest(Request):
        async def body(self) -> bytes:
            if not hasattr(self, "_body"):
                body = await super().body()
                if "gzip" in self.headers.getlist("Content-Encoding"):
                    body = gzip.decompress(body)
                self._body = body
            return self._body
    
    
    class GzipRoute(APIRoute):
        def get_route_handler(self) -> Callable:
            original_route_handler = super().get_route_handler()
    
            async def custom_route_handler(request: Request) -> Response:
                request = GzipRequest(request.scope, request.receive)
                return await original_route_handler(request)
    
            return custom_route_handler
    
    
    app = FastAPI()
    app.router.route_class = GzipRoute
    
    
    @app.post("/sum")
    async def sum_numbers(numbers: list[int] = Body()):
        return {"sum": sum(numbers)}
    

```

Технические детали

У `Request` есть атрибут `request.scope` — это просто Python-`dict`, содержащий метаданные, связанные с HTTP-запросом.

У `Request` также есть `request.receive` — функция для «получения» тела запроса.

И `dict` `scope`, и функция `receive` являются частью спецификации ASGI.

Именно этих двух компонентов — `scope` и `receive` — достаточно, чтобы создать новый экземпляр `Request`.

Чтобы узнать больше о `Request`, см. [документацию Starlette о запросах](https://www.starlette.dev/requests/).

Единственное, что делает по-другому функция, возвращённая `GzipRequest.get_route_handler`, — преобразует `Request` в `GzipRequest`.

Благодаря этому наш `GzipRequest` позаботится о распаковке данных (при необходимости) до передачи их в наши _операции пути_.

Дальше вся логика обработки остаётся прежней.

Но благодаря изменениям в `GzipRequest.body` тело запроса будет автоматически распаковано при необходимости, когда оно будет загружено **FastAPI**.

## Доступ к телу запроса в обработчике исключений

Совет

Для решения этой задачи, вероятно, намного проще использовать `body` в пользовательском обработчике `RequestValidationError` ([Обработка ошибок](https://fastapi.tiangolo.com/ru/tutorial/handling-errors/#use-the-requestvalidationerror-body) ([local](./../06_учебник-руководство-пользователя/24_обработка-ошибок.md#use-the-requestvalidationerror-body))).

Но этот пример всё равно актуален и показывает, как взаимодействовать с внутренними компонентами.

Тем же подходом можно воспользоваться, чтобы получить доступ к телу запроса в обработчике исключений.

Нужно лишь обработать запрос внутри блока `try`/`except`:

Python 3.10+

```
 
    from collections.abc import Callable
    from typing import Annotated
    
    from fastapi import Body, FastAPI, HTTPException, Request, Response
    from fastapi.exceptions import RequestValidationError
    from fastapi.routing import APIRoute
    
    
    class ValidationErrorLoggingRoute(APIRoute):
        def get_route_handler(self) -> Callable:
            original_route_handler = super().get_route_handler()
    
            async def custom_route_handler(request: Request) -> Response:
                try:
                    return await original_route_handler(request)
                except RequestValidationError as exc:
                    body = await request.body()
                    detail = {"errors": exc.errors(), "body": body.decode()}
                    raise HTTPException(status_code=422, detail=detail)
    
            return custom_route_handler
    
    
    app = FastAPI()
    app.router.route_class = ValidationErrorLoggingRoute
    
    
    @app.post("/")
    async def sum_numbers(numbers: Annotated[list[int], Body()]):
        return sum(numbers)
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from collections.abc import Callable
    
    from fastapi import Body, FastAPI, HTTPException, Request, Response
    from fastapi.exceptions import RequestValidationError
    from fastapi.routing import APIRoute
    
    
    class ValidationErrorLoggingRoute(APIRoute):
        def get_route_handler(self) -> Callable:
            original_route_handler = super().get_route_handler()
    
            async def custom_route_handler(request: Request) -> Response:
                try:
                    return await original_route_handler(request)
                except RequestValidationError as exc:
                    body = await request.body()
                    detail = {"errors": exc.errors(), "body": body.decode()}
                    raise HTTPException(status_code=422, detail=detail)
    
            return custom_route_handler
    
    
    app = FastAPI()
    app.router.route_class = ValidationErrorLoggingRoute
    
    
    @app.post("/")
    async def sum_numbers(numbers: list[int] = Body()):
        return sum(numbers)
    

```

Если произойдёт исключение, экземпляр `Request` всё ещё будет в области видимости, поэтому мы сможем прочитать тело запроса и использовать его при обработке ошибки:

Python 3.10+

```
 
    from collections.abc import Callable
    from typing import Annotated
    
    from fastapi import Body, FastAPI, HTTPException, Request, Response
    from fastapi.exceptions import RequestValidationError
    from fastapi.routing import APIRoute
    
    
    class ValidationErrorLoggingRoute(APIRoute):
        def get_route_handler(self) -> Callable:
            original_route_handler = super().get_route_handler()
    
            async def custom_route_handler(request: Request) -> Response:
                try:
                    return await original_route_handler(request)
                except RequestValidationError as exc:
                    body = await request.body()
                    detail = {"errors": exc.errors(), "body": body.decode()}
                    raise HTTPException(status_code=422, detail=detail)
    
            return custom_route_handler
    
    
    app = FastAPI()
    app.router.route_class = ValidationErrorLoggingRoute
    
    
    @app.post("/")
    async def sum_numbers(numbers: Annotated[list[int], Body()]):
        return sum(numbers)
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from collections.abc import Callable
    
    from fastapi import Body, FastAPI, HTTPException, Request, Response
    from fastapi.exceptions import RequestValidationError
    from fastapi.routing import APIRoute
    
    
    class ValidationErrorLoggingRoute(APIRoute):
        def get_route_handler(self) -> Callable:
            original_route_handler = super().get_route_handler()
    
            async def custom_route_handler(request: Request) -> Response:
                try:
                    return await original_route_handler(request)
                except RequestValidationError as exc:
                    body = await request.body()
                    detail = {"errors": exc.errors(), "body": body.decode()}
                    raise HTTPException(status_code=422, detail=detail)
    
            return custom_route_handler
    
    
    app = FastAPI()
    app.router.route_class = ValidationErrorLoggingRoute
    
    
    @app.post("/")
    async def sum_numbers(numbers: list[int] = Body()):
        return sum(numbers)
    

```

## Пользовательский класс `APIRoute` в роутере

Вы также можете задать параметр `route_class` у `APIRouter`:

Python 3.10+

```
 
    import time
    from collections.abc import Callable
    
    from fastapi import APIRouter, FastAPI, Request, Response
    from fastapi.routing import APIRoute
    
    
    class TimedRoute(APIRoute):
        def get_route_handler(self) -> Callable:
            original_route_handler = super().get_route_handler()
    
            async def custom_route_handler(request: Request) -> Response:
                before = time.time()
                response: Response = await original_route_handler(request)
                duration = time.time() - before
                response.headers["X-Response-Time"] = str(duration)
                print(f"route duration: {duration}")
                print(f"route response: {response}")
                print(f"route response headers: {response.headers}")
                return response
    
            return custom_route_handler
    
    
    app = FastAPI()
    router = APIRouter(route_class=TimedRoute)
    
    
    @app.get("/")
    async def not_timed():
        return {"message": "Not timed"}
    
    
    @router.get("/timed")
    async def timed():
        return {"message": "It's the time of my life"}
    
    
    app.include_router(router)
    

```

В этом примере _операции пути_ , объявленные в `router`, будут использовать пользовательский класс `TimedRoute` и получат дополнительный HTTP-заголовок `X-Response-Time` в ответе с временем, затраченным на формирование ответа:

Python 3.10+

```
 
    import time
    from collections.abc import Callable
    
    from fastapi import APIRouter, FastAPI, Request, Response
    from fastapi.routing import APIRoute
    
    
    class TimedRoute(APIRoute):
        def get_route_handler(self) -> Callable:
            original_route_handler = super().get_route_handler()
    
            async def custom_route_handler(request: Request) -> Response:
                before = time.time()
                response: Response = await original_route_handler(request)
                duration = time.time() - before
                response.headers["X-Response-Time"] = str(duration)
                print(f"route duration: {duration}")
                print(f"route response: {response}")
                print(f"route response headers: {response.headers}")
                return response
    
            return custom_route_handler
    
    
    app = FastAPI()
    router = APIRouter(route_class=TimedRoute)
    
    
    @app.get("/")
    async def not_timed():
        return {"message": "Not timed"}
    
    
    @router.get("/timed")
    async def timed():
        return {"message": "It's the time of my life"}
    
    
    app.include_router(router)
    

```
