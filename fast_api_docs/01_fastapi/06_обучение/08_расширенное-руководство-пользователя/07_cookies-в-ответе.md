---
title: Cookies в ответе
source: https://fastapi.tiangolo.com/ru/advanced/response-cookies/
---

# Cookies в ответе

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/advanced/response-cookies/)

## Использование параметра `Response`

Вы можете объявить параметр типа `Response` в вашей функции-обработчике пути.

Затем установить cookies в этом временном объекте ответа.

Python 3.10+

```
 
    from fastapi import FastAPI, Response
    
    app = FastAPI()
    
    
    @app.post("/cookie-and-object/")
    def create_cookie(response: Response):
        response.set_cookie(key="fakesession", value="fake-cookie-session-value")
        return {"message": "Come to the dark side, we have cookies"}
    

```

После этого можно вернуть любой объект, как и раньше (например, `dict`, объект модели базы данных и так далее).

Если вы указали `response_model`, он всё равно будет использоваться для фильтрации и преобразования возвращаемого объекта.

**FastAPI** извлечет cookies (а также HTTP-заголовки и статус-код) из временного ответа и включит их в окончательный ответ, содержащий ваше возвращаемое значение, отфильтрованное через `response_model`.

Вы также можете объявить параметр типа `Response` в зависимостях и устанавливать cookies (и HTTP-заголовки) там.

## Возвращение `Response` напрямую

Вы также можете установить Cookies, если возвращаете `Response` напрямую в вашем коде.

Для этого создайте объект `Response`, как описано в разделе [Возвращение ответа напрямую](https://fastapi.tiangolo.com/ru/advanced/response-directly/) ([local](./04_возврат-ответа-напрямую.md)).

Затем установите cookies и верните этот объект:

Python 3.10+

```
 
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    
    app = FastAPI()
    
    
    @app.post("/cookie/")
    def create_cookie():
        content = {"message": "Come to the dark side, we have cookies"}
        response = JSONResponse(content=content)
        response.set_cookie(key="fakesession", value="fake-cookie-session-value")
        return response
    

```

Совет

Имейте в виду, что если вы возвращаете ответ напрямую, вместо использования параметра `Response`, FastAPI вернёт его напрямую.

Убедитесь, что ваши данные имеют корректный тип. Например, они должны быть совместимы с JSON, если вы возвращаете `JSONResponse`.

Также убедитесь, что вы не отправляете данные, которые должны были быть отфильтрованы через `response_model`.

### Дополнительная информация

Технические детали

Вы также можете использовать `from starlette.responses import Response` или `from starlette.responses import JSONResponse`.

**FastAPI** предоставляет `fastapi.responses`, которые являются теми же объектами, что и `starlette.responses`, просто для удобства. Однако большинство доступных типов ответов поступает непосредственно из **Starlette**.

И так как `Response` часто используется для установки HTTP-заголовков и cookies, **FastAPI** также предоставляет его как `fastapi.Response`.

Чтобы увидеть все доступные параметры и настройки, ознакомьтесь с [документацией Starlette](https://www.starlette.dev/responses/#set-cookie).
