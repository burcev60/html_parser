---
title: URL-адреса метаданных и документации
source: https://fastapi.tiangolo.com/ru/tutorial/metadata/
---

# URL-адреса метаданных и документации

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/tutorial/metadata/)

Вы можете настроить несколько конфигураций метаданных в вашем **FastAPI** приложении.

## Метаданные для API

Вы можете задать следующие поля, которые используются в спецификации OpenAPI и в UI автоматической документации API:

Параметр | Тип | Описание  
---|---|---  
`title` | `str` | Заголовок API.  
`summary` | `str` | Краткое резюме API. Доступно начиная с OpenAPI 3.1.0, FastAPI 0.99.0.  
`description` | `str` | Краткое описание API. Может быть использован Markdown.  
`version` | `string` | Версия API. Версия вашего собственного приложения, а не OpenAPI. К примеру `2.5.0`.  
`terms_of_service` | `str` | Ссылка к условиям пользования API. Если указано, то это должен быть URL-адрес.  
`contact` | `dict` | Контактная информация для открытого API. Может содержать несколько полей. поля `contact`| Параметр| Тип| Описание  
---|---|---  
`name`| `str`| Идентификационное имя контактного лица/организации.  
`url`| `str`| URL указывающий на контактную информацию. ДОЛЖЕН быть в формате URL.  
`email`| `str`| Email адрес контактного лица/организации. ДОЛЖЕН быть в формате email адреса.  
`license_info` | `dict` | Информация о лицензии открытого API. Может содержать несколько полей. поля `license_info`| Параметр| Тип| Описание  
---|---|---  
`name`| `str`| **ОБЯЗАТЕЛЬНО** (если установлен параметр `license_info`). Название лицензии, используемой для API.  
`identifier`| `str`| Выражение лицензии [SPDX](https://spdx.org/licenses/) для API. Поле `identifier` взаимоисключающее с полем `url`. Доступно начиная с OpenAPI 3.1.0, FastAPI 0.99.0.  
`url`| `str`| URL, указывающий на лицензию, используемую для API. ДОЛЖЕН быть в формате URL.  
  
Вы можете задать их следующим образом:

Python 3.10+

```
 
    from fastapi import FastAPI
    
    description = """
    ChimichangApp API helps you do awesome stuff. 🚀
    
    ## Items
    
    You can **read items**.
    
    ## Users
    
    You will be able to:
    
    * **Create users** (_not implemented_).
    * **Read users** (_not implemented_).
    """
    
    app = FastAPI(
        title="ChimichangApp",
        description=description,
        summary="Deadpool's favorite app. Nuff said.",
        version="0.0.1",
        terms_of_service="http://example.com/terms/",
        contact={
            "name": "Deadpoolio the Amazing",
            "url": "http://x-force.example.com/contact/",
            "email": "dp@x-force.example.com",
        },
        license_info={
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        },
    )
    
    
    @app.get("/items/")
    async def read_items():
        return [{"name": "Katana"}]
    

```

Подсказка

Вы можете использовать Markdown в поле `description`, и оно будет отображено в выводе.

С этой конфигурацией автоматическая документация API будет выглядеть так:

![](https://fastapi.tiangolo.com/img/tutorial/metadata/image01.png)

## Идентификатор лицензии

Начиная с OpenAPI 3.1.0 и FastAPI 0.99.0, вы также можете задать `license_info` с помощью `identifier` вместо `url`.

К примеру:

Python 3.10+

```
 
    from fastapi import FastAPI
    
    description = """
    ChimichangApp API helps you do awesome stuff. 🚀
    
    ## Items
    
    You can **read items**.
    
    ## Users
    
    You will be able to:
    
    * **Create users** (_not implemented_).
    * **Read users** (_not implemented_).
    """
    
    app = FastAPI(
        title="ChimichangApp",
        description=description,
        summary="Deadpool's favorite app. Nuff said.",
        version="0.0.1",
        terms_of_service="http://example.com/terms/",
        contact={
            "name": "Deadpoolio the Amazing",
            "url": "http://x-force.example.com/contact/",
            "email": "dp@x-force.example.com",
        },
        license_info={
            "name": "Apache 2.0",
            "identifier": "Apache-2.0",
        },
    )
    
    
    @app.get("/items/")
    async def read_items():
        return [{"name": "Katana"}]
    

```

## Метаданные для тегов

Вы также можете добавить дополнительные метаданные для различных тегов, используемых для группировки ваших операций пути с помощью параметра `openapi_tags`.

Он принимает список, содержащий один словарь для каждого тега.

Каждый словарь может содержать в себе:

  * `name` (**обязательно**): `str`-значение с тем же именем тега, которое вы используете в параметре `tags` в ваших _операциях пути_ и `APIRouter`ах.
  * `description`: `str`-значение с кратким описанием для тега. Может содержать Markdown и будет отображаться в UI документации.
  * `externalDocs`: `dict`-значение описывающее внешнюю документацию. Включает в себя:
    * `description`: `str`-значение с кратким описанием для внешней документации.
    * `url` (**обязательно**): `str`-значение с URL-адресом для внешней документации.

### Создание метаданных для тегов

Давайте попробуем сделать это на примере с тегами для `users` и `items`.

Создайте метаданные для ваших тегов и передайте их в параметре `openapi_tags`:

Python 3.10+

```
 
    from fastapi import FastAPI
    
    tags_metadata = [
        {
            "name": "users",
            "description": "Operations with users. The **login** logic is also here.",
        },
        {
            "name": "items",
            "description": "Manage items. So _fancy_ they have their own docs.",
            "externalDocs": {
                "description": "Items external docs",
                "url": "https://fastapi.tiangolo.com/",
            },
        },
    ]
    
    app = FastAPI(openapi_tags=tags_metadata)
    
    
    @app.get("/users/", tags=["users"])
    async def get_users():
        return [{"name": "Harry"}, {"name": "Ron"}]
    
    
    @app.get("/items/", tags=["items"])
    async def get_items():
        return [{"name": "wand"}, {"name": "flying broom"}]
    

```

Помните, что вы можете использовать Markdown внутри описания, к примеру "login" будет отображен жирным шрифтом (**login**) и "fancy" будет отображаться курсивом (_fancy_).

Подсказка

Вам необязательно добавлять метаданные для всех используемых тегов

### Используйте собственные теги

Используйте параметр `tags` с вашими _операциями пути_ (и `APIRouter`ами), чтобы присвоить им различные теги:

Python 3.10+

```
 
    from fastapi import FastAPI
    
    tags_metadata = [
        {
            "name": "users",
            "description": "Operations with users. The **login** logic is also here.",
        },
        {
            "name": "items",
            "description": "Manage items. So _fancy_ they have their own docs.",
            "externalDocs": {
                "description": "Items external docs",
                "url": "https://fastapi.tiangolo.com/",
            },
        },
    ]
    
    app = FastAPI(openapi_tags=tags_metadata)
    
    
    @app.get("/users/", tags=["users"])
    async def get_users():
        return [{"name": "Harry"}, {"name": "Ron"}]
    
    
    @app.get("/items/", tags=["items"])
    async def get_items():
        return [{"name": "wand"}, {"name": "flying broom"}]
    

```

Дополнительная информация

Узнайте больше о тегах в [Конфигурации операции пути](https://fastapi.tiangolo.com/ru/tutorial/path-operation-configuration/#tags) ([local](./25_конфигурация-операций-пути.md#tags)).

### Проверьте документацию

Теперь, если вы проверите документацию, вы увидите всю дополнительную информацию:

![](https://fastapi.tiangolo.com/img/tutorial/metadata/image02.png)

### Порядок расположения тегов

Порядок расположения словарей метаданных для каждого тега определяет также порядок, отображаемый в UI документации.

К примеру, несмотря на то, что `users` будут идти после `items` в алфавитном порядке, они отображаются раньше, потому что мы добавляем свои метаданные в качестве первого словаря в списке.

## URL-адрес OpenAPI

По умолчанию схема OpenAPI отображена по адресу `/openapi.json`.

Но вы можете изменить это с помощью параметра `openapi_url`.

К примеру, чтобы задать её отображение по адресу `/api/v1/openapi.json`:

Python 3.10+

```
 
    from fastapi import FastAPI
    
    app = FastAPI(openapi_url="/api/v1/openapi.json")
    
    
    @app.get("/items/")
    async def read_items():
        return [{"name": "Foo"}]
    

```

Если вы хотите отключить схему OpenAPI полностью, вы можете задать `openapi_url=None`, это также отключит пользовательские интерфейсы документации, которые её используют.

## URL-адреса документации

Вы можете изменить конфигурацию двух пользовательских интерфейсов документации, которые включены:

  * **Swagger UI** : отображаемый по адресу `/docs`.
    * Вы можете задать его URL с помощью параметра `docs_url`.
    * Вы можете отключить это с помощью настройки `docs_url=None`.
  * **ReDoc** : отображаемый по адресу `/redoc`.
    * Вы можете задать его URL с помощью параметра `redoc_url`.
    * Вы можете отключить это с помощью настройки `redoc_url=None`.

К примеру, чтобы задать отображение Swagger UI по адресу `/documentation` и отключить ReDoc:

Python 3.10+

```
 
    from fastapi import FastAPI
    
    app = FastAPI(docs_url="/documentation", redoc_url=None)
    
    
    @app.get("/items/")
    async def read_items():
        return [{"name": "Foo"}]
    

```
