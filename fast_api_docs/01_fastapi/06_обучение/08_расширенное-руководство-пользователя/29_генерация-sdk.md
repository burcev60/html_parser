---
title: Генерация SDK
source: https://fastapi.tiangolo.com/ru/advanced/generate-clients/
---

# Генерация SDK

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/advanced/generate-clients/)

Поскольку **FastAPI** основан на спецификации **OpenAPI** , его API можно описать в стандартном формате, понятном множеству инструментов.

Это упрощает генерацию актуальной **документации** , клиентских библиотек (**SDKs**) на разных языках, а также **тестирования** или **воркфлоу автоматизации** , которые остаются синхронизированными с вашим кодом.

В этом руководстве вы узнаете, как сгенерировать **TypeScript SDK** для вашего бэкенда на FastAPI.

## Генераторы SDK с открытым исходным кодом

Гибкий вариант — [OpenAPI Generator](https://openapi-generator.tech/), который поддерживает **многие языки программирования** и умеет генерировать SDK из вашей спецификации OpenAPI.

Для **TypeScript‑клиентов** [Hey API](https://heyapi.dev/) — специализированное решение, обеспечивающее оптимальный опыт для экосистемы TypeScript.

Больше генераторов SDK можно найти на [OpenAPI.Tools](https://openapi.tools/#sdk).

Совет

FastAPI автоматически генерирует спецификации **OpenAPI 3.1** , поэтому любой используемый инструмент должен поддерживать эту версию.

## Генераторы SDK от спонсоров FastAPI

В этом разделе представлены решения с **венчурной поддержкой** и **поддержкой компаний** от компаний, которые спонсируют FastAPI. Эти продукты предоставляют **дополнительные возможности** и **интеграции** сверх высококачественно генерируемых SDK.

Благодаря ✨ [**спонсорству FastAPI**](https://fastapi.tiangolo.com/ru/help-fastapi/#sponsor-the-author) ([local](./../../11_ресурсы/01_помочь-fastapi-получить-помощь.md#sponsor-the-author)) ✨ эти компании помогают обеспечивать, чтобы фреймворк и его **экосистема** оставались здоровыми и **устойчивыми**.

Их спонсорство также демонстрирует серьёзную приверженность **сообществу** FastAPI (вам), показывая, что им важно не только предоставлять **отличный сервис** , но и поддерживать **надёжный и процветающий фреймворк** FastAPI. 🙇

Например, вы можете попробовать:

  * [Speakeasy](https://speakeasy.com/editor?utm_source=fastapi+repo&utm_medium=github+sponsorship)
  * [Stainless](https://www.stainless.com/?utm_source=fastapi&utm_medium=referral)
  * [liblab](https://developers.liblab.com/tutorials/sdk-for-fastapi?utm_source=fastapi)

Некоторые из этих решений также могут быть open source или иметь бесплатные тарифы, так что вы сможете попробовать их без финансовых затрат. Другие коммерческие генераторы SDK доступны и их можно найти онлайн. 🤓

## Создать TypeScript SDK

Начнём с простого приложения FastAPI:

Python 3.10+

```
 
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        price: float
    
    
    class ResponseMessage(BaseModel):
        message: str
    
    
    @app.post("/items/", response_model=ResponseMessage)
    async def create_item(item: Item):
        return {"message": "item received"}
    
    
    @app.get("/items/", response_model=list[Item])
    async def get_items():
        return [
            {"name": "Plumbus", "price": 3},
            {"name": "Portal Gun", "price": 9001},
        ]
    

```

Обратите внимание, что _операции пути (обработчики пути)_ определяют модели, которые они используют для полезной нагрузки запроса и полезной нагрузки ответа, с помощью моделей `Item` и `ResponseMessage`.

### Документация API

Если перейти на `/docs`, вы увидите **схемы** данных, отправляемых в запросах и принимаемых в ответах:

![](https://fastapi.tiangolo.com/img/tutorial/generate-clients/image01.png)

Вы видите эти схемы, потому что они были объявлены с моделями в приложении.

Эта информация доступна в **схеме OpenAPI** приложения и затем отображается в документации API.

Та же информация из моделей, включённая в OpenAPI, может использоваться для **генерации клиентского кода**.

### Hey API

Как только у нас есть приложение FastAPI с моделями, мы можем использовать Hey API для генерации TypeScript‑клиента. Самый быстрый способ сделать это — через npx.

```
 
    npx @hey-api/openapi-ts -i http://localhost:8000/openapi.json -o src/client
    

```

Это сгенерирует TypeScript SDK в `./src/client`.

Вы можете узнать, как [установить `@hey-api/openapi-ts`](https://heyapi.dev/openapi-ts/get-started) и почитать о [сгенерированном результате](https://heyapi.dev/openapi-ts/output) на их сайте.

### Использование SDK

Теперь вы можете импортировать и использовать клиентский код. Это может выглядеть так, обратите внимание, что вы получаете автозавершение для методов:

![](https://fastapi.tiangolo.com/img/tutorial/generate-clients/image02.png)

Вы также получите автозавершение для отправляемой полезной нагрузки:

![](https://fastapi.tiangolo.com/img/tutorial/generate-clients/image03.png)

Совет

Обратите внимание на автозавершение для `name` и `price`, это было определено в приложении FastAPI, в модели `Item`.

Вы получите ошибки прямо в редакторе для отправляемых данных:

![](https://fastapi.tiangolo.com/img/tutorial/generate-clients/image04.png)

Объект ответа также будет иметь автозавершение:

![](https://fastapi.tiangolo.com/img/tutorial/generate-clients/image05.png)

## Приложение FastAPI с тегами

Во многих случаях ваше приложение FastAPI будет больше, и вы, вероятно, будете использовать теги, чтобы разделять разные группы _операций пути_.

Например, у вас может быть раздел для **items** и другой раздел для **users** , и они могут быть разделены тегами:

Python 3.10+

```
 
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        price: float
    
    
    class ResponseMessage(BaseModel):
        message: str
    
    
    class User(BaseModel):
        username: str
        email: str
    
    
    @app.post("/items/", response_model=ResponseMessage, tags=["items"])
    async def create_item(item: Item):
        return {"message": "Item received"}
    
    
    @app.get("/items/", response_model=list[Item], tags=["items"])
    async def get_items():
        return [
            {"name": "Plumbus", "price": 3},
            {"name": "Portal Gun", "price": 9001},
        ]
    
    
    @app.post("/users/", response_model=ResponseMessage, tags=["users"])
    async def create_user(user: User):
        return {"message": "User received"}
    

```

### Генерация TypeScript‑клиента с тегами

Если вы генерируете клиент для приложения FastAPI с использованием тегов, обычно клиентский код также будет разделён по тегам.

Таким образом вы сможете иметь всё правильно упорядоченным и сгруппированным в клиентском коде:

![](https://fastapi.tiangolo.com/img/tutorial/generate-clients/image06.png)

В этом случае у вас есть:

  * `ItemsService`
  * `UsersService`

### Имена методов клиента

Сейчас сгенерированные имена методов вроде `createItemItemsPost` выглядят не очень аккуратно:

```
 
    ItemsService.createItemItemsPost({name: "Plumbus", price: 5})
    

```

...это потому, что генератор клиента использует внутренний **ID операции** OpenAPI для каждой _операции пути_.

OpenAPI требует, чтобы каждый ID операции был уникален среди всех _операций пути_ , поэтому FastAPI использует **имя функции** , **путь** и **HTTP‑метод/операцию** для генерации этого ID операции, так как таким образом можно гарантировать уникальность ID операций.

Но далее я покажу, как это улучшить. 🤓

## Пользовательские ID операций и лучшие имена методов

Вы можете **изменить** способ **генерации** этих ID операций, чтобы сделать их проще, а имена методов в клиентах — **более простыми**.

В этом случае вам нужно будет обеспечить, чтобы каждый ID операции был **уникальным** другим способом.

Например, вы можете гарантировать, что у каждой _операции пути_ есть тег, и затем генерировать ID операции на основе **тега** и **имени** _операции пути_ (имени функции).

### Пользовательская функция генерации уникального ID

FastAPI использует **уникальный ID** для каждой _операции пути_ , который применяется для **ID операции** , а также для имён любых необходимых пользовательских моделей запросов или ответов.

Вы можете кастомизировать эту функцию. Она принимает `APIRoute` и возвращает строку.

Например, здесь берётся первый тег (скорее всего у вас один тег) и имя _операции пути_ (имя функции).

Затем вы можете передать эту пользовательскую функцию в **FastAPI** через параметр `generate_unique_id_function`:

Python 3.10+

```
 
    from fastapi import FastAPI
    from fastapi.routing import APIRoute
    from pydantic import BaseModel
    
    
    def custom_generate_unique_id(route: APIRoute):
        return f"{route.tags[0]}-{route.name}"
    
    
    app = FastAPI(generate_unique_id_function=custom_generate_unique_id)
    
    
    class Item(BaseModel):
        name: str
        price: float
    
    
    class ResponseMessage(BaseModel):
        message: str
    
    
    class User(BaseModel):
        username: str
        email: str
    
    
    @app.post("/items/", response_model=ResponseMessage, tags=["items"])
    async def create_item(item: Item):
        return {"message": "Item received"}
    
    
    @app.get("/items/", response_model=list[Item], tags=["items"])
    async def get_items():
        return [
            {"name": "Plumbus", "price": 3},
            {"name": "Portal Gun", "price": 9001},
        ]
    
    
    @app.post("/users/", response_model=ResponseMessage, tags=["users"])
    async def create_user(user: User):
        return {"message": "User received"}
    

```

### Генерация TypeScript‑клиента с пользовательскими ID операций

Теперь, если снова сгенерировать клиент, вы увидите, что имена методов улучшились:

![](https://fastapi.tiangolo.com/img/tutorial/generate-clients/image07.png)

Как видите, теперь имена методов содержат тег, а затем имя функции; больше они не включают информацию из URL‑пути и HTTP‑операции.

### Предобработка спецификации OpenAPI для генератора клиента

В сгенерированном коде всё ещё есть **дублирующаяся информация**.

Мы уже знаем, что этот метод относится к **items** , потому что это слово есть в `ItemsService` (взято из тега), но при этом имя тега всё ещё добавлено префиксом к имени метода. 😕

Скорее всего мы захотим оставить это в OpenAPI в целом, так как это гарантирует, что ID операций будут **уникальны**.

Но для сгенерированного клиента мы можем **модифицировать** ID операций OpenAPI непосредственно перед генерацией клиентов, чтобы сделать имена методов более приятными и **чистыми**.

Мы можем скачать OpenAPI JSON в файл `openapi.json`, а затем **убрать этот префикс‑тег** таким скриптом:

Python 3.10+Node.js

```
 
    import json
    from pathlib import Path
    
    file_path = Path("./openapi.json")
    openapi_content = json.loads(file_path.read_text())
    
    for path_data in openapi_content["paths"].values():
        for operation in path_data.values():
            tag = operation["tags"][0]
            operation_id = operation["operationId"]
            to_remove = f"{tag}-"
            new_operation_id = operation_id[len(to_remove) :]
            operation["operationId"] = new_operation_id
    
    file_path.write_text(json.dumps(openapi_content))
    

```

```
 
    import * as fs from 'fs'
    
    async function modifyOpenAPIFile(filePath) {
      try {
        const data = await fs.promises.readFile(filePath)
        const openapiContent = JSON.parse(data)
    
        const paths = openapiContent.paths
        for (const pathKey of Object.keys(paths)) {
          const pathData = paths[pathKey]
          for (const method of Object.keys(pathData)) {
            const operation = pathData[method]
            if (operation.tags && operation.tags.length > 0) {
              const tag = operation.tags[0]
              const operationId = operation.operationId
              const toRemove = `${tag}-`
              if (operationId.startsWith(toRemove)) {
                const newOperationId = operationId.substring(toRemove.length)
                operation.operationId = newOperationId
              }
            }
          }
        }
    
        await fs.promises.writeFile(
          filePath,
          JSON.stringify(openapiContent, null, 2),
        )
        console.log('File successfully modified')
      } catch (err) {
        console.error('Error:', err)
      }
    }
    
    const filePath = './openapi.json'
    modifyOpenAPIFile(filePath)
    

```

После этого ID операций будут переименованы с чего‑то вроде `items-get_items` просто в `get_items`, и генератор клиента сможет создавать более простые имена методов.

### Генерация TypeScript‑клиента с предобработанным OpenAPI

Так как конечный результат теперь в файле `openapi.json`, нужно обновить входное расположение:

```
 
    npx @hey-api/openapi-ts -i ./openapi.json -o src/client
    

```

После генерации нового клиента у вас будут **чистые имена методов** , со всем **автозавершением** , **ошибками прямо в редакторе** и т.д.:

![](https://fastapi.tiangolo.com/img/tutorial/generate-clients/image08.png)

## Преимущества

При использовании автоматически сгенерированных клиентов вы получите **автозавершение** для:

  * Методов.
  * Данных запроса — в теле запроса, query‑параметрах и т.д.
  * Данных ответа.

У вас также будут **ошибки прямо в редакторе** для всего.

И каждый раз, когда вы обновляете код бэкенда и **перегенерируете** фронтенд, в нём появятся новые _операции пути_ как методы, старые будут удалены, а любые другие изменения отразятся в сгенерированном коде. 🤓

Это также означает, что если что‑то изменилось, это будет **отражено** в клиентском коде автоматически. И если вы **соберёте** клиент, он завершится с ошибкой, если где‑то есть **несоответствие** в используемых данных.

Таким образом, вы **обнаружите многие ошибки** очень рано в цикле разработки, вместо того чтобы ждать, когда ошибки проявятся у конечных пользователей в продакшн, и затем пытаться отладить, в чём проблема. ✨
  *[**SDKs**]: Software Development Kits - Наборы средств разработки
