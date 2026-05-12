---
title: Модели Query-Параметров
source: https://fastapi.tiangolo.com/ru/tutorial/query-param-models/
---

# Модели Query-Параметров

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/tutorial/query-param-models/)

Если у вас есть группа связанных **query-параметров** , то вы можете объединить их в одну **Pydantic-модель**.

Это позволит вам **переиспользовать модель** в **разных местах** , устанавливать валидаторы и метаданные, в том числе для сразу всех параметров, в одном месте. 😎

Заметка

Это поддерживается начиная с версии FastAPI `0.115.0`. 🤓

## Pydantic-Модель для Query-Параметров

Объявите нужные **query-параметры** в **Pydantic-модели** , а после аннотируйте параметр как `Query`:

Python 3.10+

```
 
    from typing import Annotated, Literal
    
    from fastapi import FastAPI, Query
    from pydantic import BaseModel, Field
    
    app = FastAPI()
    
    
    class FilterParams(BaseModel):
        limit: int = Field(100, gt=0, le=100)
        offset: int = Field(0, ge=0)
        order_by: Literal["created_at", "updated_at"] = "created_at"
        tags: list[str] = []
    
    
    @app.get("/items/")
    async def read_items(filter_query: Annotated[FilterParams, Query()]):
        return filter_query
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from typing import Literal
    
    from fastapi import FastAPI, Query
    from pydantic import BaseModel, Field
    
    app = FastAPI()
    
    
    class FilterParams(BaseModel):
        limit: int = Field(100, gt=0, le=100)
        offset: int = Field(0, ge=0)
        order_by: Literal["created_at", "updated_at"] = "created_at"
        tags: list[str] = []
    
    
    @app.get("/items/")
    async def read_items(filter_query: FilterParams = Query()):
        return filter_query
    

```

**FastAPI извлечёт** данные соответствующие **каждому полю модели** из **query-параметров** запроса и выдаст вам объявленную Pydantic-модель заполненную ими.

## Проверьте Сгенерированную Документацию

Вы можете посмотреть query-параметры в графическом интерфейсе сгенерированной документации по пути `/docs`:

![](https://fastapi.tiangolo.com/img/tutorial/query-param-models/image01.png)

## Запретить Дополнительные Query-Параметры

В некоторых случаях (не особо часто встречающихся) вам может понадобиться **ограничить** query-параметры, которые вы хотите получить.

Вы можете сконфигурировать Pydantic-модель так, чтобы запретить (`forbid`) все дополнительные (`extra`) поля.

Python 3.10+

```
 
    from typing import Annotated, Literal
    
    from fastapi import FastAPI, Query
    from pydantic import BaseModel, Field
    
    app = FastAPI()
    
    
    class FilterParams(BaseModel):
        model_config = {"extra": "forbid"}
    
        limit: int = Field(100, gt=0, le=100)
        offset: int = Field(0, ge=0)
        order_by: Literal["created_at", "updated_at"] = "created_at"
        tags: list[str] = []
    
    
    @app.get("/items/")
    async def read_items(filter_query: Annotated[FilterParams, Query()]):
        return filter_query
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from typing import Literal
    
    from fastapi import FastAPI, Query
    from pydantic import BaseModel, Field
    
    app = FastAPI()
    
    
    class FilterParams(BaseModel):
        model_config = {"extra": "forbid"}
    
        limit: int = Field(100, gt=0, le=100)
        offset: int = Field(0, ge=0)
        order_by: Literal["created_at", "updated_at"] = "created_at"
        tags: list[str] = []
    
    
    @app.get("/items/")
    async def read_items(filter_query: FilterParams = Query()):
        return filter_query
    

```

Если клиент попробует отправить **дополнительные** данные в **query-параметрах** , то в ответ он получит **ошибку**.

Например, если клиент попытается отправить query-параметр `tool` с значением `plumbus`, в виде:

```
 
    https://example.com/items/?limit=10&tool=plumbus
    

```

То в ответ он получит **ошибку** , сообщающую ему, что query-параметр `tool` не разрешен:

```
 
    {
        "detail": [
            {
                "type": "extra_forbidden",
                "loc": ["query", "tool"],
                "msg": "Extra inputs are not permitted",
                "input": "plumbus"
            }
        ]
    }
    

```

## Заключение

Вы можете использовать **Pydantic-модели** для объявления **query-параметров** в **FastAPI**. 😎

Совет

Спойлер: вы также можете использовать Pydantic-модели, чтобы объявлять cookies и HTTP-заголовки, но об этом вы прочитаете позже. 🤫
