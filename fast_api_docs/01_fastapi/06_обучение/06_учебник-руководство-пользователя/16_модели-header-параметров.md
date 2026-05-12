---
title: Модели Header-параметров
source: https://fastapi.tiangolo.com/ru/tutorial/header-param-models/
---

# Модели Header-параметров

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/tutorial/header-param-models/)

Если у вас есть группа связанных **header-параметров** , то вы можете объединить их в одну **Pydantic-модель**.

Это позволит вам **переиспользовать модель** в **разных местах** , а также задать валидацию и метаданные сразу для всех параметров. 😎

Заметка

Этот функционал доступен в FastAPI начиная с версии `0.115.0`. 🤓

## Header-параметры в виде Pydantic-модели

Объявите нужные **header-параметры** в **Pydantic-модели** и затем аннотируйте параметр как `Header`:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Header
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class CommonHeaders(BaseModel):
        host: str
        save_data: bool
        if_modified_since: str | None = None
        traceparent: str | None = None
        x_tag: list[str] = []
    
    
    @app.get("/items/")
    async def read_items(headers: Annotated[CommonHeaders, Header()]):
        return headers
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Header
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class CommonHeaders(BaseModel):
        host: str
        save_data: bool
        if_modified_since: str | None = None
        traceparent: str | None = None
        x_tag: list[str] = []
    
    
    @app.get("/items/")
    async def read_items(headers: CommonHeaders = Header()):
        return headers
    

```

**FastAPI** **извлечёт** данные для **каждого поля** из **заголовков** запроса и выдаст заданную вами Pydantic-модель.

## Проверьте документацию

Вы можете посмотреть нужные header-параметры в графическом интерфейсе сгенерированной документации по пути `/docs`:

![](https://fastapi.tiangolo.com/img/tutorial/header-param-models/image01.png)

## Как запретить дополнительные заголовки

В некоторых случаях (не особо часто встречающихся) вам может понадобиться **ограничить** заголовки, которые вы хотите получать.

Вы можете использовать возможности конфигурации Pydantic-модели для того, чтобы запретить (`forbid`) любые дополнительные (`extra`) поля:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Header
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class CommonHeaders(BaseModel):
        model_config = {"extra": "forbid"}
    
        host: str
        save_data: bool
        if_modified_since: str | None = None
        traceparent: str | None = None
        x_tag: list[str] = []
    
    
    @app.get("/items/")
    async def read_items(headers: Annotated[CommonHeaders, Header()]):
        return headers
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Header
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class CommonHeaders(BaseModel):
        model_config = {"extra": "forbid"}
    
        host: str
        save_data: bool
        if_modified_since: str | None = None
        traceparent: str | None = None
        x_tag: list[str] = []
    
    
    @app.get("/items/")
    async def read_items(headers: CommonHeaders = Header()):
        return headers
    

```

Если клиент попробует отправить **дополнительные заголовки** , то в ответ он получит **ошибку**.

Например, если клиент попытается отправить заголовок `tool` со значением `plumbus`, то в ответ он получит ошибку, сообщающую ему, что header-параметр `tool` не разрешен:

```
 
    {
        "detail": [
            {
                "type": "extra_forbidden",
                "loc": ["header", "tool"],
                "msg": "Extra inputs are not permitted",
                "input": "plumbus",
            }
        ]
    }
    

```

## Как отключить автоматическое преобразование подчеркиваний

Как и в случае с обычными заголовками, если у вас в именах параметров имеются символы подчеркивания, они **автоматически преобразовываются в дефис**.

Например, если в коде есть header-параметр `save_data`, то ожидаемый HTTP-заголовок будет `save-data` и именно так он будет отображаться в документации.

Если по каким-то причинам вам нужно отключить данное автоматическое преобразование, это можно сделать и для Pydantic-моделей для header-параметров.

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Header
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class CommonHeaders(BaseModel):
        host: str
        save_data: bool
        if_modified_since: str | None = None
        traceparent: str | None = None
        x_tag: list[str] = []
    
    
    @app.get("/items/")
    async def read_items(
        headers: Annotated[CommonHeaders, Header(convert_underscores=False)],
    ):
        return headers
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Header
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class CommonHeaders(BaseModel):
        host: str
        save_data: bool
        if_modified_since: str | None = None
        traceparent: str | None = None
        x_tag: list[str] = []
    
    
    @app.get("/items/")
    async def read_items(headers: CommonHeaders = Header(convert_underscores=False)):
        return headers
    

```

Внимание

Перед тем как устанавливать для параметра `convert_underscores` значение `False`, имейте в виду, что некоторые HTTP-прокси и серверы не разрешают использовать заголовки с символами подчеркивания.

## Резюме

Вы можете использовать **Pydantic-модели** для объявления **header-параметров** в **FastAPI**. 😎
