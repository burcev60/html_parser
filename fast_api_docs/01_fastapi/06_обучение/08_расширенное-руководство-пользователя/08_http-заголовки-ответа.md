---
title: HTTP-заголовки ответа
source: https://fastapi.tiangolo.com/ru/advanced/response-headers/
---

# HTTP-заголовки ответа

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/advanced/response-headers/)

## Использовать параметр `Response`

Вы можете объявить параметр типа `Response` в вашей функции-обработчике пути (как можно сделать и для cookie).

А затем вы можете устанавливать HTTP-заголовки в этом _временном_ объекте ответа.

Python 3.10+

```
 
    from fastapi import FastAPI, Response
    
    app = FastAPI()
    
    
    @app.get("/headers-and-object/")
    def get_headers(response: Response):
        response.headers["X-Cat-Dog"] = "alone in the world"
        return {"message": "Hello World"}
    

```

После этого вы можете вернуть любой нужный объект, как обычно (например, `dict`, модель из базы данных и т.д.).

И, если вы объявили `response_model`, он всё равно будет использован для фильтрации и преобразования возвращённого объекта.

**FastAPI** использует этот _временный_ ответ, чтобы извлечь HTTP-заголовки (а также cookie и статус-код) и поместит их в финальный HTTP-ответ, который содержит возвращённое вами значение, отфильтрованное согласно `response_model`.

Вы также можете объявлять параметр `Response` в зависимостях и устанавливать в них заголовки (и cookie).

## Вернуть `Response` напрямую

Вы также можете добавить HTTP-заголовки, когда возвращаете `Response` напрямую.

Создайте ответ, как описано в [Вернуть Response напрямую](https://fastapi.tiangolo.com/ru/advanced/response-directly/) ([local](./04_возврат-ответа-напрямую.md)), и передайте заголовки как дополнительный параметр:

Python 3.10+

```
 
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    
    app = FastAPI()
    
    
    @app.get("/headers/")
    def get_headers():
        content = {"message": "Hello World"}
        headers = {"X-Cat-Dog": "alone in the world", "Content-Language": "en-US"}
        return JSONResponse(content=content, headers=headers)
    

```

Технические детали

Вы также можете использовать `from starlette.responses import Response` или `from starlette.responses import JSONResponse`.

**FastAPI** предоставляет те же самые `starlette.responses` как `fastapi.responses` — для вашего удобства как разработчика. Но большинство доступных классов ответов поступают напрямую из Starlette.

И поскольку `Response` часто используется для установки заголовков и cookie, **FastAPI** также предоставляет его как `fastapi.Response`.

## Пользовательские HTTP-заголовки

Помните, что собственные проприетарные заголовки можно добавлять, [используя префикс `X-`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers).

Но если у вас есть пользовательские заголовки, которые вы хотите показывать клиенту в браузере, вам нужно добавить их в настройки CORS (подробнее см. в [CORS (Cross-Origin Resource Sharing)](https://fastapi.tiangolo.com/ru/tutorial/cors/) ([local](./../06_учебник-руководство-пользователя/33_cors-cross-origin-resource-sharing.md))), используя параметр `expose_headers`, описанный в [документации Starlette по CORS](https://www.starlette.dev/middleware/#corsmiddleware).
