---
title: Расширение OpenAPI
source: https://fastapi.tiangolo.com/ru/how-to/extending-openapi/
---

# Расширение OpenAPI

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/how-to/extending-openapi/)

Иногда может понадобиться изменить сгенерированную схему OpenAPI.

В этом разделе показано, как это сделать.

## Обычный процесс

Обычный (по умолчанию) процесс выглядит так.

Приложение `FastAPI` (экземпляр) имеет метод `.openapi()`, который должен возвращать схему OpenAPI.

В процессе создания объекта приложения регистрируется _операция пути_ (обработчик пути) для `/openapi.json` (или для того, что указано в вашем `openapi_url`).

Она просто возвращает JSON-ответ с результатом вызова метода приложения `.openapi()`.

По умолчанию метод `.openapi()` проверяет свойство `.openapi_schema`: если в нём уже есть данные, возвращает их.

Если нет — генерирует схему с помощью вспомогательной функции `fastapi.openapi.utils.get_openapi`.

Функция `get_openapi()` принимает параметры:

  * `title`: Заголовок OpenAPI, отображается в документации.
  * `version`: Версия вашего API, например `2.5.0`.
  * `openapi_version`: Версия используемой спецификации OpenAPI. По умолчанию — последняя: `3.1.0`.
  * `summary`: Краткое описание API.
  * `description`: Описание вашего API; может включать Markdown и будет отображаться в документации.
  * `routes`: Список маршрутов — это каждая зарегистрированная _операция пути_. Берутся из `app.routes`.

Информация

Параметр `summary` доступен в OpenAPI 3.1.0 и выше, поддерживается FastAPI версии 0.99.0 и выше.

## Переопределение значений по умолчанию

Используя информацию выше, вы можете той же вспомогательной функцией сгенерировать схему OpenAPI и переопределить любые нужные части.

Например, добавим [расширение OpenAPI ReDoc для включения собственного логотипа](https://github.com/Rebilly/ReDoc/blob/master/docs/redoc-vendor-extensions.md#x-logo).

### Обычный **FastAPI**

Сначала напишите приложение **FastAPI** как обычно:

Python 3.10+

```
 
    from fastapi import FastAPI
    from fastapi.openapi.utils import get_openapi
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items():
        return [{"name": "Foo"}]
    
    
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title="Custom title",
            version="2.5.0",
            summary="This is a very custom OpenAPI schema",
            description="Here's a longer description of the custom **OpenAPI** schema",
            routes=app.routes,
        )
        openapi_schema["info"]["x-logo"] = {
            "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
        }
        app.openapi_schema = openapi_schema
        return app.openapi_schema
    
    
    app.openapi = custom_openapi
    

```

### Сгенерируйте схему OpenAPI

Затем используйте ту же вспомогательную функцию для генерации схемы OpenAPI внутри функции `custom_openapi()`:

Python 3.10+

```
 
    from fastapi import FastAPI
    from fastapi.openapi.utils import get_openapi
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items():
        return [{"name": "Foo"}]
    
    
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title="Custom title",
            version="2.5.0",
            summary="This is a very custom OpenAPI schema",
            description="Here's a longer description of the custom **OpenAPI** schema",
            routes=app.routes,
        )
        openapi_schema["info"]["x-logo"] = {
            "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
        }
        app.openapi_schema = openapi_schema
        return app.openapi_schema
    
    
    app.openapi = custom_openapi
    

```

### Измените схему OpenAPI

Теперь можно добавить расширение ReDoc, добавив кастомный `x-logo` в «объект» `info` в схеме OpenAPI:

Python 3.10+

```
 
    from fastapi import FastAPI
    from fastapi.openapi.utils import get_openapi
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items():
        return [{"name": "Foo"}]
    
    
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title="Custom title",
            version="2.5.0",
            summary="This is a very custom OpenAPI schema",
            description="Here's a longer description of the custom **OpenAPI** schema",
            routes=app.routes,
        )
        openapi_schema["info"]["x-logo"] = {
            "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
        }
        app.openapi_schema = openapi_schema
        return app.openapi_schema
    
    
    app.openapi = custom_openapi
    

```

### Кэшируйте схему OpenAPI

Вы можете использовать свойство `.openapi_schema` как «кэш» для хранения сгенерированной схемы.

Так приложению не придётся генерировать схему каждый раз, когда пользователь открывает документацию API.

Она будет создана один раз, а затем тот же кэшированный вариант будет использоваться для последующих запросов.

Python 3.10+

```
 
    from fastapi import FastAPI
    from fastapi.openapi.utils import get_openapi
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items():
        return [{"name": "Foo"}]
    
    
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title="Custom title",
            version="2.5.0",
            summary="This is a very custom OpenAPI schema",
            description="Here's a longer description of the custom **OpenAPI** schema",
            routes=app.routes,
        )
        openapi_schema["info"]["x-logo"] = {
            "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
        }
        app.openapi_schema = openapi_schema
        return app.openapi_schema
    
    
    app.openapi = custom_openapi
    

```

### Переопределите метод

Теперь вы можете заменить метод `.openapi()` на вашу новую функцию.

Python 3.10+

```
 
    from fastapi import FastAPI
    from fastapi.openapi.utils import get_openapi
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items():
        return [{"name": "Foo"}]
    
    
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title="Custom title",
            version="2.5.0",
            summary="This is a very custom OpenAPI schema",
            description="Here's a longer description of the custom **OpenAPI** schema",
            routes=app.routes,
        )
        openapi_schema["info"]["x-logo"] = {
            "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
        }
        app.openapi_schema = openapi_schema
        return app.openapi_schema
    
    
    app.openapi = custom_openapi
    

```

### Проверьте

Перейдите на <http://127.0.0.1:8000/redoc> — вы увидите, что используется ваш кастомный логотип (в этом примере — логотип **FastAPI**):

![](https://fastapi.tiangolo.com/img/tutorial/extending-openapi/image01.png)
