---
title: Стриминг JSON Lines
source: https://fastapi.tiangolo.com/ru/tutorial/stream-json-lines/
---

# Стриминг JSON Lines

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/tutorial/stream-json-lines/)

У вас может быть последовательность данных, которую вы хотите отправлять в «**потоке** ». Это можно сделать с помощью **JSON Lines**.

Информация

Добавлено в FastAPI 0.134.0.

## Что такое поток?

«**Стриминг** » данных означает, что ваше приложение начнет отправлять элементы данных клиенту, не дожидаясь готовности всей последовательности.

То есть оно отправит первый элемент, клиент его получит и начнет обрабатывать, а вы в это время можете все еще генерировать следующий элемент.

```
 
    sequenceDiagram
        participant App
        participant Client
    
        App->>App: Produce Item 1
        App->>Client: Send Item 1
        App->>App: Produce Item 2
        Client->>Client: Process Item 1
        App->>Client: Send Item 2
        App->>App: Produce Item 3
        Client->>Client: Process Item 2
        App->>Client: Send Item 3
        Client->>Client: Process Item 3
        Note over App: Keeps producing...
        Note over Client: Keeps consuming...

```

Это может быть даже бесконечный поток, когда вы продолжаете отправлять данные.

## JSON Lines

В таких случаях часто отправляют «**JSON Lines** », это формат, в котором отправляется по одному JSON-объекту на строку.

Ответ будет иметь тип содержимого `application/jsonl` (вместо `application/json`), а тело ответа будет примерно таким:

```
 
    {"name": "Plumbus", "description": "A multi-purpose household device."}
    {"name": "Portal Gun", "description": "A portal opening device."}
    {"name": "Meeseeks Box", "description": "A box that summons a Meeseeks."}
    

```

Это очень похоже на JSON-массив (эквивалент списка Python), но вместо того чтобы быть обернутым в `[]` и иметь `,` между элементами, здесь **один JSON-объект на строку** , они разделены символом новой строки.

Информация

Важный момент в том, что ваше приложение сможет по очереди производить каждую строку, пока клиент потребляет предыдущие строки.

Технические детали

Так как каждый JSON-объект будет разделен новой строкой, в их содержимом не могут быть буквальные символы новой строки, но могут быть экранированные переводы строк (`\n`), что входит в стандарт JSON.

Однако обычно об этом не нужно беспокоиться — всё делается автоматически, читайте дальше. 🤓

## Варианты использования

Вы можете использовать это для стриминга данных из сервиса **AI LLM** , из **логов** или **телеметрии** , или из других типов данных, которые можно структурировать в элементы **JSON**.

Совет

Если вы хотите стримить бинарные данные, например видео или аудио, посмотрите расширенное руководство: [Потоковая передача данных](https://fastapi.tiangolo.com/ru/advanced/stream-data/) ([local](./../08_расширенное-руководство-пользователя/01_потоковая-передача-данных.md)).

## Стриминг JSON Lines с FastAPI

Чтобы стримить JSON Lines с FastAPI, вместо использования `return` в вашей _функции-обработчике пути_ используйте `yield`, чтобы по очереди выдавать каждый элемент.

Python 3.10+

```
 
    from collections.abc import AsyncIterable, Iterable
    
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        description: str | None
    
    
    items = [
        Item(name="Plumbus", description="A multi-purpose household device."),
        Item(name="Portal Gun", description="A portal opening device."),
        Item(name="Meeseeks Box", description="A box that summons a Meeseeks."),
    ]
    
    
    @app.get("/items/stream")
    async def stream_items() -> AsyncIterable[Item]:
        for item in items:
            yield item
    
    # Code below omitted 👇
    

```

👀 Full file preview

Python 3.10+

```
 
    from collections.abc import AsyncIterable, Iterable
    
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        description: str | None
    
    
    items = [
        Item(name="Plumbus", description="A multi-purpose household device."),
        Item(name="Portal Gun", description="A portal opening device."),
        Item(name="Meeseeks Box", description="A box that summons a Meeseeks."),
    ]
    
    
    @app.get("/items/stream")
    async def stream_items() -> AsyncIterable[Item]:
        for item in items:
            yield item
    
    
    @app.get("/items/stream-no-async")
    def stream_items_no_async() -> Iterable[Item]:
        for item in items:
            yield item
    
    
    @app.get("/items/stream-no-annotation")
    async def stream_items_no_annotation():
        for item in items:
            yield item
    
    
    @app.get("/items/stream-no-async-no-annotation")
    def stream_items_no_async_no_annotation():
        for item in items:
            yield item
    

```

Если каждый JSON-элемент, который вы хотите отправить обратно, имеет тип `Item` (Pydantic-модель), и это асинхронная функция, вы можете объявить тип возвращаемого значения как `AsyncIterable[Item]`:

Python 3.10+

```
 
    from collections.abc import AsyncIterable, Iterable
    
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        description: str | None
    
    
    items = [
        Item(name="Plumbus", description="A multi-purpose household device."),
        Item(name="Portal Gun", description="A portal opening device."),
        Item(name="Meeseeks Box", description="A box that summons a Meeseeks."),
    ]
    
    
    @app.get("/items/stream")
    async def stream_items() -> AsyncIterable[Item]:
        for item in items:
            yield item
    
    # Code below omitted 👇
    

```

👀 Full file preview

Python 3.10+

```
 
    from collections.abc import AsyncIterable, Iterable
    
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        description: str | None
    
    
    items = [
        Item(name="Plumbus", description="A multi-purpose household device."),
        Item(name="Portal Gun", description="A portal opening device."),
        Item(name="Meeseeks Box", description="A box that summons a Meeseeks."),
    ]
    
    
    @app.get("/items/stream")
    async def stream_items() -> AsyncIterable[Item]:
        for item in items:
            yield item
    
    
    @app.get("/items/stream-no-async")
    def stream_items_no_async() -> Iterable[Item]:
        for item in items:
            yield item
    
    
    @app.get("/items/stream-no-annotation")
    async def stream_items_no_annotation():
        for item in items:
            yield item
    
    
    @app.get("/items/stream-no-async-no-annotation")
    def stream_items_no_async_no_annotation():
        for item in items:
            yield item
    

```

Если вы объявите тип возвращаемого значения, FastAPI будет использовать его, чтобы **валидировать** данные, **документировать** их в OpenAPI, **фильтровать** и **сериализовать** с помощью Pydantic.

Совет

Так как Pydantic будет сериализовывать это на стороне **Rust** , вы получите значительно более высокую **производительность** , чем если бы вы не указывали тип возвращаемого значения.

### Неасинхронные функции-обработчики пути

Вы также можете использовать обычные функции `def` (без `async`) и использовать `yield` таким же образом.

FastAPI обеспечит корректное выполнение так, чтобы это не блокировало цикл событий.

Поскольку в этом случае функция не асинхронная, подходящим типом возвращаемого значения будет `Iterable[Item]`:

Python 3.10+

```
 
    # Code above omitted 👆
    
    @app.get("/items/stream-no-async")
    def stream_items_no_async() -> Iterable[Item]:
        for item in items:
            yield item
    
    # Code below omitted 👇
    

```

👀 Full file preview

Python 3.10+

```
 
    from collections.abc import AsyncIterable, Iterable
    
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        description: str | None
    
    
    items = [
        Item(name="Plumbus", description="A multi-purpose household device."),
        Item(name="Portal Gun", description="A portal opening device."),
        Item(name="Meeseeks Box", description="A box that summons a Meeseeks."),
    ]
    
    
    @app.get("/items/stream")
    async def stream_items() -> AsyncIterable[Item]:
        for item in items:
            yield item
    
    
    @app.get("/items/stream-no-async")
    def stream_items_no_async() -> Iterable[Item]:
        for item in items:
            yield item
    
    
    @app.get("/items/stream-no-annotation")
    async def stream_items_no_annotation():
        for item in items:
            yield item
    
    
    @app.get("/items/stream-no-async-no-annotation")
    def stream_items_no_async_no_annotation():
        for item in items:
            yield item
    

```

### Без возвращаемого типа

Вы также можете опустить тип возвращаемого значения. Тогда FastAPI использует [`jsonable_encoder`](https://fastapi.tiangolo.com/ru/tutorial/encoder/) ([local](./26_json-совместимый-кодировщик.md)), чтобы преобразовать данные к виду, который можно сериализовать в JSON, и затем отправит их как JSON Lines.

Python 3.10+

```
 
    # Code above omitted 👆
    
    @app.get("/items/stream-no-annotation")
    async def stream_items_no_annotation():
        for item in items:
            yield item
    
    # Code below omitted 👇
    

```

👀 Full file preview

Python 3.10+

```
 
    from collections.abc import AsyncIterable, Iterable
    
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        description: str | None
    
    
    items = [
        Item(name="Plumbus", description="A multi-purpose household device."),
        Item(name="Portal Gun", description="A portal opening device."),
        Item(name="Meeseeks Box", description="A box that summons a Meeseeks."),
    ]
    
    
    @app.get("/items/stream")
    async def stream_items() -> AsyncIterable[Item]:
        for item in items:
            yield item
    
    
    @app.get("/items/stream-no-async")
    def stream_items_no_async() -> Iterable[Item]:
        for item in items:
            yield item
    
    
    @app.get("/items/stream-no-annotation")
    async def stream_items_no_annotation():
        for item in items:
            yield item
    
    
    @app.get("/items/stream-no-async-no-annotation")
    def stream_items_no_async_no_annotation():
        for item in items:
            yield item
    

```

## События, отправляемые сервером (SSE)

FastAPI также имеет полноценную поддержку Server-Sent Events (SSE), которые довольно похожи, но с парой дополнительных деталей. Вы можете узнать о них в следующей главе: [События, отправляемые сервером (SSE)](https://fastapi.tiangolo.com/ru/tutorial/server-sent-events/) ([local](./37_события-отправляемые-сервером-sse.md)). 🤓
