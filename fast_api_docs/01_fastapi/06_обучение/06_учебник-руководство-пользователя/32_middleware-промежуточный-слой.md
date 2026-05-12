---
title: Middleware (Промежуточный слой)
source: https://fastapi.tiangolo.com/ru/tutorial/middleware/
---

# Middleware (Промежуточный слой)

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/tutorial/middleware/)

Вы можете добавить middleware (промежуточный слой) в **FastAPI** приложение.

"Middleware" - это функция, которая выполняется с каждым **запросом** до его обработки какой-либо конкретной _операцией пути_. А также с каждым **ответом** перед его возвращением.

  * Она принимает каждый поступающий **запрос**.
  * Может что-то сделать с этим **запросом** или выполнить любой нужный код.
  * Затем передает **запрос** для последующей обработки (какой-либо _операцией пути_).
  * Получает **ответ** (от _операции пути_).
  * Может что-то сделать с этим **ответом** или выполнить любой нужный код.
  * И возвращает **ответ**.

Технические детали

Если у вас есть зависимости с `yield`, то код выхода (код после `yield`) будет выполняться _после_ middleware.

Если были какие‑либо фоновые задачи (рассматриваются в разделе [Фоновые задачи](https://fastapi.tiangolo.com/ru/tutorial/background-tasks/) ([local](./38_фоновые-задачи.md)), вы увидите это позже), они будут запущены _после_ всех middleware.

## Создание middleware

Для создания middleware используйте декоратор `@app.middleware("http")` поверх функции.

Функция middleware получает:

  * `request`.
  * Функцию `call_next`, которая получает `request` в качестве параметра.
    * Эта функция передаёт `request` соответствующей _операции пути_.
    * Затем она возвращает `response`, сгенерированный соответствующей _операцией пути_.
  * Также имеется возможность видоизменить `response` перед тем как его вернуть.

Python 3.10+

```
 
    import time
    
    from fastapi import FastAPI, Request
    
    app = FastAPI()
    
    
    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        start_time = time.perf_counter()
        response = await call_next(request)
        process_time = time.perf_counter() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response
    

```

Совет

Имейте в виду, что можно добавлять проприетарные HTTP-заголовки [с префиксом `X-`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers).

Но если вы хотите, чтобы клиент в браузере мог видеть ваши пользовательские заголовки, необходимо добавить их в настройки CORS ([CORS (Cross-Origin Resource Sharing)](https://fastapi.tiangolo.com/ru/tutorial/cors/) ([local](./33_cors-cross-origin-resource-sharing.md))), используя параметр `expose_headers`, описанный в [документации по CORS Starlette](https://www.starlette.dev/middleware/#corsmiddleware).

Технические детали

Вы также можете использовать `from starlette.requests import Request`.

**FastAPI** предоставляет такой доступ для удобства разработчиков. Но, на самом деле, это `Request` из Starlette.

### До и после `response`

Вы можете добавить код, использующий `request`, до передачи его какой-либо _операции пути_.

А также после формирования `response`, до того, как вы его вернёте.

Например, вы можете добавить собственный заголовок `X-Process-Time`, содержащий время в секундах, необходимое для обработки запроса и генерации ответа:

Python 3.10+

```
 
    import time
    
    from fastapi import FastAPI, Request
    
    app = FastAPI()
    
    
    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        start_time = time.perf_counter()
        response = await call_next(request)
        process_time = time.perf_counter() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response
    

```

Совет

Мы используем [`time.perf_counter()`](https://docs.python.org/3/library/time.html#time.perf_counter) вместо `time.time()` для обеспечения большей точности в таких случаях. 🤓

## Порядок выполнения нескольких middleware

Когда вы добавляете несколько middleware с помощью декоратора `@app.middleware()` или метода `app.add_middleware()`, каждое новое middleware оборачивает приложение, формируя стек. Последнее добавленное middleware — самое внешнее (_outermost_), а первое — самое внутреннее (_innermost_).

На пути обработки запроса сначала выполняется самое внешнее middleware.

На пути формирования ответа оно выполняется последним.

Например:

```
 
    app.add_middleware(MiddlewareA)
    app.add_middleware(MiddlewareB)
    

```

Это приводит к следующему порядку выполнения:

  * **Запрос** : MiddlewareB → MiddlewareA → маршрут

  * **Ответ** : маршрут → MiddlewareA → MiddlewareB

Такое стековое поведение обеспечивает предсказуемый и управляемый порядок выполнения middleware.

## Другие middleware

О других middleware вы можете узнать больше в разделе [Расширенное руководство пользователя: Продвинутое middleware](https://fastapi.tiangolo.com/ru/advanced/middleware/) ([local](./../08_расширенное-руководство-пользователя/15_расширенное-использование-middleware.md)).

В следующем разделе вы можете прочитать, как настроить CORS с помощью middleware.
  *[CORS]: Cross-Origin Resource Sharing - совместное использование ресурсов между источниками
