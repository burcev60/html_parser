---
title: Body - Поля
source: https://fastapi.tiangolo.com/ru/tutorial/body-fields/
---

# Body - Поля

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/tutorial/body-fields/)

Таким же способом, как вы объявляете дополнительную валидацию и метаданные в параметрах _функции обработки пути_ с помощью функций `Query`, `Path` и `Body`, вы можете объявлять валидацию и метаданные внутри Pydantic моделей, используя функцию `Field` из Pydantic.

## Импорт `Field`

Сначала вы должны импортировать его:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import Body, FastAPI
    from pydantic import BaseModel, Field
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        description: str | None = Field(
            default=None, title="The description of the item", max_length=300
        )
        price: float = Field(gt=0, description="The price must be greater than zero")
        tax: float | None = None
    
    
    @app.put("/items/{item_id}")
    async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
        results = {"item_id": item_id, "item": item}
        return results
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import Body, FastAPI
    from pydantic import BaseModel, Field
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        description: str | None = Field(
            default=None, title="The description of the item", max_length=300
        )
        price: float = Field(gt=0, description="The price must be greater than zero")
        tax: float | None = None
    
    
    @app.put("/items/{item_id}")
    async def update_item(item_id: int, item: Item = Body(embed=True)):
        results = {"item_id": item_id, "item": item}
        return results
    

```

Внимание

Обратите внимание, что функция `Field` импортируется непосредственно из `pydantic`, а не из `fastapi`, как все остальные функции (`Query`, `Path`, `Body` и т.д.).

## Объявление атрибутов модели

Вы можете использовать функцию `Field` с атрибутами модели:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import Body, FastAPI
    from pydantic import BaseModel, Field
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        description: str | None = Field(
            default=None, title="The description of the item", max_length=300
        )
        price: float = Field(gt=0, description="The price must be greater than zero")
        tax: float | None = None
    
    
    @app.put("/items/{item_id}")
    async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
        results = {"item_id": item_id, "item": item}
        return results
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import Body, FastAPI
    from pydantic import BaseModel, Field
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        description: str | None = Field(
            default=None, title="The description of the item", max_length=300
        )
        price: float = Field(gt=0, description="The price must be greater than zero")
        tax: float | None = None
    
    
    @app.put("/items/{item_id}")
    async def update_item(item_id: int, item: Item = Body(embed=True)):
        results = {"item_id": item_id, "item": item}
        return results
    

```

Функция `Field` работает так же, как `Query`, `Path` и `Body`, у неё такие же параметры и т.д.

Технические детали

На самом деле, `Query`, `Path` и другие функции, которые вы увидите в дальнейшем, создают объекты подклассов общего класса `Param`, который сам по себе является подклассом `FieldInfo` из Pydantic.

И `Field` (из Pydantic) также возвращает экземпляр `FieldInfo`.

`Body` также напрямую возвращает объекты подкласса `FieldInfo`. И есть и другие, с которыми вы познакомитесь позже, которые являются подклассами класса `Body`.

Помните, что когда вы импортируете `Query`, `Path` и другое из `fastapi`, это фактически функции, которые возвращают специальные классы.

Подсказка

Обратите внимание, что каждый атрибут модели с типом, значением по умолчанию и `Field` имеет ту же структуру, что и параметр _функции обработки пути_ с `Field` вместо `Path`, `Query` и `Body`.

## Добавление дополнительной информации

Вы можете объявлять дополнительную информацию в `Field`, `Query`, `Body` и т.п. Она будет включена в сгенерированную JSON схему.

Вы узнаете больше о добавлении дополнительной информации позже в документации, когда будете изучать, как задавать примеры.

Внимание

Дополнительные ключи, переданные в функцию `Field`, также будут присутствовать в сгенерированной OpenAPI схеме вашего приложения. Поскольку эти ключи не являются обязательной частью спецификации OpenAPI, некоторые инструменты OpenAPI, например, [валидатор OpenAPI](https://validator.swagger.io/), могут не работать с вашей сгенерированной схемой.

## Резюме

Вы можете использовать функцию `Field` из Pydantic, чтобы задавать дополнительную валидацию и метаданные для атрибутов модели.

Вы также можете использовать дополнительные ключевые аргументы, чтобы добавить метаданные JSON схемы.
