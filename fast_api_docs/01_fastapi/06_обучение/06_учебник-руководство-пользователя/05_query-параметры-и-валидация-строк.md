---
title: Query-параметры и валидация строк
source: https://fastapi.tiangolo.com/ru/tutorial/query-params-str-validations/
---

# Query-параметры и валидация строк

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/)

**FastAPI** позволяет определять дополнительную информацию и выполнять валидацию для ваших параметров.

Рассмотрим это приложение в качестве примера:

Python 3.10+

```
 
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: str | None = None):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

Query-параметр `q` имеет тип `str | None`, это означает, что он имеет тип `str`, но также может быть `None`. Значение по умолчанию действительно `None`, поэтому FastAPI будет знать, что он не обязателен.

Примечание

FastAPI поймёт, что значение `q` не обязательно, из‑за значения по умолчанию `= None`.

Аннотация `str | None` позволит вашему редактору кода обеспечить лучшую поддержку и находить ошибки.

## Дополнительная валидация

Мы собираемся добавить ограничение: хотя `q` и необязателен, когда он передан, **его длина не должна превышать 50 символов**.

### Импорт `Query` и `Annotated`

Чтобы сделать это, сначала импортируйте:

  * `Query` из `fastapi`
  * `Annotated` из `typing`

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: str | None = Query(default=None, max_length=50)):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

Дополнительная информация

Поддержка `Annotated` (и рекомендация использовать его) появилась в FastAPI версии 0.95.0.

Если у вас более старая версия, при попытке использовать `Annotated` вы получите ошибки.

Убедитесь, что вы [обновили версию FastAPI](https://fastapi.tiangolo.com/ru/deployment/versions/#upgrading-the-fastapi-versions) ([local](./../12_развёртывание/01_о-версиях-fastapi.md#upgrading-the-fastapi-versions)) как минимум до 0.95.1 перед использованием `Annotated`.

## Использовать `Annotated` в типе для параметра `q`

Помните, я уже говорил, что `Annotated` можно использовать для добавления метаданных к параметрам в разделе [Введение в типы Python](https://fastapi.tiangolo.com/ru/python-types/#type-hints-with-metadata-annotations) ([local](./../01_введение-в-типы-python.md#type-hints-with-metadata-annotations))?

Пришло время использовать его с FastAPI. 🚀

У нас была такая аннотация типа:

```
 
    q: str | None = None
    

```

Мы «обернём» это в `Annotated`, и получится:

```
 
    q: Annotated[str | None] = None
    

```

Обе версии означают одно и то же: `q` — параметр, который может быть `str` или `None`, и по умолчанию равен `None`.

А теперь к самому интересному. 🎉

## Добавим `Query` в `Annotated` для параметра `q`

Теперь, когда у нас есть `Annotated`, куда можно поместить дополнительную информацию (в нашем случае — дополнительные правила валидации), добавим `Query` внутрь `Annotated` и установим параметр `max_length` равным `50`:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: str | None = Query(default=None, max_length=50)):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

Обратите внимание, что значение по умолчанию по‑прежнему `None`, то есть параметр остаётся необязательным.

Но теперь, добавив `Query(max_length=50)` внутрь `Annotated`, мы говорим FastAPI, что этому значению нужна **дополнительная валидация** — максимум 50 символов. 😎

Совет

Здесь мы используем `Query()`, потому что это **query-параметр**. Позже мы увидим другие — `Path()`, `Body()`, `Header()` и `Cookie()`, — они также принимают те же аргументы, что и `Query()`.

Теперь FastAPI будет:

  * **валидировать** данные, удостоверяясь, что максимальная длина — 50 символов;
  * показывать **понятную ошибку** клиенту, если данные невалидны;
  * **документировать** параметр в _операции пути_ схемы OpenAPI (он будет показан в **UI автоматической документации**).

## Альтернатива (устаревшее): `Query` как значение по умолчанию

В предыдущих версиях FastAPI (до 0.95.0) требовалось использовать `Query` как значение по умолчанию для параметра вместо помещения его в `Annotated`. Скорее всего вы ещё встретите такой код, поэтому поясню.

Подсказка

Для нового кода и везде, где это возможно, используйте `Annotated`, как описано выше. У этого есть несколько преимуществ (см. ниже) и нет недостатков. 🍰

Вот как можно использовать `Query()` как значение по умолчанию для параметра функции, установив `max_length` равным 50:

Python 3.10+ - non-Annotated

```
 
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: str | None = Query(default=None, max_length=50)):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

🤓 Other versions and variants

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

Так как в этом случае (без `Annotated`) мы заменяем в функции значение по умолчанию `None` на `Query()`, теперь нужно указать значение по умолчанию через параметр `Query(default=None)`, это служит той же цели — задать значение по умолчанию (по крайней мере для FastAPI).

Итак:

```
 
    q: str | None = Query(default=None)
    

```

...делает параметр необязательным со значением по умолчанию `None`, так же как:

```
 
    q: str | None = None
    

```

Но вариант с `Query` явно объявляет его как query-параметр.

Затем мы можем передать и другие параметры в `Query`. В данном случае — параметр `max_length`, применимый к строкам:

```
 
    q: str | None = Query(default=None, max_length=50)
    

```

Это провалидирует данные, покажет понятную ошибку, если данные невалидны, и задокументирует параметр в _операции пути_ схемы OpenAPI.

### `Query` как значение по умолчанию или внутри `Annotated`

Помните, что при использовании `Query` внутри `Annotated` нельзя указывать параметр `default` у `Query`.

Вместо этого используйте обычное значение по умолчанию параметра функции. Иначе это будет неоднозначно.

Например, так делать нельзя:

```
 
    q: Annotated[str, Query(default="rick")] = "morty"
    

```

...потому что непонятно, какое значение должно быть по умолчанию: `"rick"` или `"morty"`.

Следовательно, используйте (предпочтительно):

```
 
    q: Annotated[str, Query()] = "rick"
    

```

...или в старой кодовой базе вы увидите:

```
 
    q: str = Query(default="rick")
    

```

### Преимущества `Annotated`

**Рекомендуется использовать`Annotated`** вместо задания значения по умолчанию в параметрах функции — так **лучше** по нескольким причинам. 🤓

**Значение по умолчанию** у **параметра функции** — это **настоящее значение по умолчанию** , что более интуитивно для Python. 😌

Вы можете **вызвать** эту же функцию в **других местах** без FastAPI, и она будет **работать как ожидается**. Если есть **обязательный** параметр (без значения по умолчанию), ваш **редактор** сообщит об ошибке, **Python** тоже пожалуется, если вы запустите её без передачи обязательного параметра.

Если вы не используете `Annotated`, а применяете **(устаревший) стиль со значением по умолчанию** , то при вызове этой функции без FastAPI в **других местах** вам нужно **помнить** о том, что надо передать аргументы, чтобы всё работало корректно, иначе значения будут не такими, как вы ожидаете (например, вместо `str` будет `QueryInfo` или что-то подобное). И ни редактор, ни Python не будут ругаться при самом вызове функции — ошибка проявится лишь при операциях внутри.

Так как `Annotated` может содержать больше одной аннотации метаданных, теперь вы можете использовать ту же функцию и с другими инструментами, например с [Typer](https://typer.tiangolo.com/). 🚀

## Больше валидаций

Можно также добавить параметр `min_length`:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(
        q: Annotated[str | None, Query(min_length=3, max_length=50)] = None,
    ):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: str | None = Query(default=None, min_length=3, max_length=50)):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

## Регулярные выражения

Вы можете определить регулярное выражение `pattern`, которому должен соответствовать параметр:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(
        q: Annotated[
            str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
        ] = None,
    ):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(
        q: str | None = Query(
            default=None, min_length=3, max_length=50, pattern="^fixedquery$"
        ),
    ):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

Данный шаблон регулярного выражения проверяет, что полученное значение параметра:

  * `^`: начинается с следующих символов, до них нет символов.
  * `fixedquery`: имеет точное значение `fixedquery`.
  * `$`: заканчивается здесь, после `fixedquery` нет никаких символов.

Если вы теряетесь во всех этих идеях про **«регулярные выражения»** , не переживайте. Это сложная тема для многих. Многое можно сделать и без них.

Теперь вы знаете, что когда они понадобятся, вы сможете использовать их в **FastAPI**.

## Значения по умолчанию

Конечно, можно использовать и другие значения по умолчанию, не только `None`.

Допустим, вы хотите объявить, что query-параметр `q` должен иметь `min_length` равный `3` и значение по умолчанию `"fixedquery"`:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: str = Query(default="fixedquery", min_length=3)):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

Примечание

Наличие значения по умолчанию любого типа, включая `None`, делает параметр необязательным.

## Обязательные параметры

Когда не требуется объявлять дополнительные проверки или метаданные, можно сделать query-параметр `q` обязательным, просто не указывая значение по умолчанию, например:

```
 
    q: str
    

```

вместо:

```
 
    q: str | None = None
    

```

Но сейчас мы объявляем его через `Query`, например так:

```
 
    q: Annotated[str | None, Query(min_length=3)] = None
    

```

Поэтому, когда вам нужно объявить значение как обязательное при использовании `Query`, просто не указывайте значение по умолчанию:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: Annotated[str, Query(min_length=3)]):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: str = Query(min_length=3)):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

### Обязательный, но может быть `None`

Можно объявить, что параметр может принимать `None`, но при этом остаётся обязательным. Это заставит клиентов отправлять значение, даже если это значение — `None`.

Для этого объявите, что `None` — валидный тип, но просто не задавайте значение по умолчанию:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: Annotated[str | None, Query(min_length=3)]):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: str | None = Query(min_length=3)):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

## Query-параметр - список / несколько значений

Когда вы явно объявляете query-параметр через `Query`, можно также указать, что он принимает список значений, иначе говоря — несколько значений.

Например, чтобы объявить query-параметр `q`, который может встречаться в URL несколько раз, можно написать:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: Annotated[list[str] | None, Query()] = None):
        query_items = {"q": q}
        return query_items
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: list[str] | None = Query(default=None)):
        query_items = {"q": q}
        return query_items
    

```

Тогда при таком URL:

```
 
    http://localhost:8000/items/?q=foo&q=bar
    

```

вы получите множественные значения _query-параметров_ `q` (`foo` и `bar`) в виде Python-`list` внутри вашей _функции-обработчика пути_ , в _параметре функции_ `q`.

Таким образом, ответ на этот URL будет:

```
 
    {
      "q": [
        "foo",
        "bar"
      ]
    }
    

```

Совет

Чтобы объявить query-параметр типа `list`, как в примере выше, нужно явно использовать `Query`, иначе он будет интерпретирован как тело запроса.

Интерактивная документация API обновится соответствующим образом и позволит передавать несколько значений:

![](https://fastapi.tiangolo.com/img/tutorial/query-params-str-validations/image02.png)

### Query-параметр - список / несколько значений со значением по умолчанию

Можно также определить значение по умолчанию как `list`, если ничего не передано:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
        query_items = {"q": q}
        return query_items
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: list[str] = Query(default=["foo", "bar"])):
        query_items = {"q": q}
        return query_items
    

```

Если вы перейдёте по адресу:

```
 
    http://localhost:8000/items/
    

```

значение по умолчанию для `q` будет: `["foo", "bar"]`, и ответом будет:

```
 
    {
      "q": [
        "foo",
        "bar"
      ]
    }
    

```

#### Просто `list`

Можно использовать `list` напрямую вместо `list[str]`:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: Annotated[list, Query()] = []):
        query_items = {"q": q}
        return query_items
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: list = Query(default=[])):
        query_items = {"q": q}
        return query_items
    

```

Примечание

Имейте в виду, что в этом случае FastAPI не будет проверять содержимое списка.

Например, `list[int]` проверит (и задокументирует), что элементы списка — целые числа. А просто `list` — нет.

## Больше метаданных

Можно добавить больше информации о параметре.

Эта информация будет включена в сгенерированную OpenAPI-схему и использована интерфейсами документации и внешними инструментами.

Примечание

Помните, что разные инструменты могут иметь разный уровень поддержки OpenAPI.

Некоторые из них пока могут не показывать всю дополнительную информацию, хотя в большинстве случаев недостающая возможность уже запланирована к разработке.

Можно задать `title`:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(
        q: Annotated[str | None, Query(title="Query string", min_length=3)] = None,
    ):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(
        q: str | None = Query(default=None, title="Query string", min_length=3),
    ):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

И `description`:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(
        q: Annotated[
            str | None,
            Query(
                title="Query string",
                description="Query string for the items to search in the database that have a good match",
                min_length=3,
            ),
        ] = None,
    ):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(
        q: str | None = Query(
            default=None,
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
        ),
    ):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

## Псевдонимы параметров

Представьте, что вы хотите, чтобы параметр назывался `item-query`.

Например:

```
 
    http://127.0.0.1:8000/items/?item-query=foobaritems
    

```

Но `item-query` — недопустимое имя переменной в Python.

Ближайший вариант — `item_query`.

Но вам всё равно нужно именно `item-query`...

Тогда можно объявить `alias`, и этот псевдоним будет использован для поиска значения параметра:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: Annotated[str | None, Query(alias="item-query")] = None):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(q: str | None = Query(default=None, alias="item-query")):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

## Маркировка параметров как устаревших

Предположим, этот параметр вам больше не нравится.

Его нужно оставить на какое‑то время, так как клиенты его используют, но вы хотите, чтобы в документации он явно отображался как устаревший.

Тогда передайте параметр `deprecated=True` в `Query`:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(
        q: Annotated[
            str | None,
            Query(
                alias="item-query",
                title="Query string",
                description="Query string for the items to search in the database that have a good match",
                min_length=3,
                max_length=50,
                pattern="^fixedquery$",
                deprecated=True,
            ),
        ] = None,
    ):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(
        q: str | None = Query(
            default=None,
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ):
        results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
        if q:
            results.update({"q": q})
        return results
    

```

В документации это будет показано так:

![](https://fastapi.tiangolo.com/img/tutorial/query-params-str-validations/image01.png)

## Исключить параметры из OpenAPI

Чтобы исключить query-параметр из генерируемой OpenAPI-схемы (и, следовательно, из систем автоматической документации), укажите у `Query` параметр `include_in_schema=False`:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(
        hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,
    ):
        if hidden_query:
            return {"hidden_query": hidden_query}
        else:
            return {"hidden_query": "Not found"}
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Query
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(
        hidden_query: str | None = Query(default=None, include_in_schema=False),
    ):
        if hidden_query:
            return {"hidden_query": hidden_query}
        else:
            return {"hidden_query": "Not found"}
    

```

## Кастомная валидация

Бывают случаи, когда нужна **кастомная валидация** , которую нельзя выразить параметрами выше.

В таких случаях можно использовать **кастомную функцию-валидатор** , которая применяется после обычной валидации (например, после проверки, что значение — это `str`).

Этого можно добиться, используя [`AfterValidator` Pydantic](https://docs.pydantic.dev/latest/concepts/validators/#field-after-validator) внутри `Annotated`.

Совет

В Pydantic также есть [`BeforeValidator`](https://docs.pydantic.dev/latest/concepts/validators/#field-before-validator) и другие. 🤓

Например, эта кастомная проверка убеждается, что ID элемента начинается с `isbn-` для номера книги ISBN или с `imdb-` для ID URL фильма на IMDB:

Python 3.10+

```
 
    import random
    from typing import Annotated
    
    from fastapi import FastAPI
    from pydantic import AfterValidator
    
    app = FastAPI()
    
    data = {
        "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
        "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
        "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
    }
    
    
    def check_valid_id(id: str):
        if not id.startswith(("isbn-", "imdb-")):
            raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
        return id
    
    
    @app.get("/items/")
    async def read_items(
        id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
    ):
        if id:
            item = data.get(id)
        else:
            id, item = random.choice(list(data.items()))
        return {"id": id, "name": item}
    

```

Дополнительная информация

Это доступно в Pydantic версии 2 и выше. 😎

Совет

Если вам нужна валидация, требующая общения с каким‑либо **внешним компонентом** — базой данных или другим API — вместо этого используйте **Зависимости FastAPI** , вы познакомитесь с ними позже.

Эти кастомные валидаторы предназначены для проверок, которые можно выполнить, имея **только** те же **данные** , что пришли в запросе.

### Понимание этого кода

Важный момент — это использовать **`AfterValidator` с функцией внутри `Annotated`**. Смело пропускайте эту часть. 🤸

* * *

Но если вам любопытен именно этот пример и всё ещё интересно, вот немного подробностей.

#### Строка и `value.startswith()`

Заметили? Метод строки `value.startswith()` может принимать кортеж — тогда будет проверено каждое значение из кортежа:

Python 3.10+

```
 
    # Code above omitted 👆
    
    def check_valid_id(id: str):
        if not id.startswith(("isbn-", "imdb-")):
            raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
        return id
    
    # Code below omitted 👇
    

```

👀 Full file preview

Python 3.10+

```
 
    import random
    from typing import Annotated
    
    from fastapi import FastAPI
    from pydantic import AfterValidator
    
    app = FastAPI()
    
    data = {
        "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
        "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
        "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
    }
    
    
    def check_valid_id(id: str):
        if not id.startswith(("isbn-", "imdb-")):
            raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
        return id
    
    
    @app.get("/items/")
    async def read_items(
        id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
    ):
        if id:
            item = data.get(id)
        else:
            id, item = random.choice(list(data.items()))
        return {"id": id, "name": item}
    

```

#### Случайный элемент

С помощью `data.items()` мы получаем итерируемый объект с кортежами, содержащими ключ и значение для каждого элемента словаря.

Мы превращаем этот итерируемый объект в обычный `list` через `list(data.items())`.

Затем с `random.choice()` можно получить **случайное значение** из списка — то есть кортеж вида `(id, name)`. Это будет что‑то вроде `("imdb-tt0371724", "The Hitchhiker's Guide to the Galaxy")`.

После этого мы **присваиваем эти два значения** кортежа переменным `id` и `name`.

Так что, если пользователь не передал ID элемента, он всё равно получит случайную рекомендацию.

...и всё это в **одной простой строке**. 🤯 Разве не прекрасен Python? 🐍

Python 3.10+

```
 
    # Code above omitted 👆
    
    @app.get("/items/")
    async def read_items(
        id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
    ):
        if id:
            item = data.get(id)
        else:
            id, item = random.choice(list(data.items()))
        return {"id": id, "name": item}
    

```

👀 Full file preview

Python 3.10+

```
 
    import random
    from typing import Annotated
    
    from fastapi import FastAPI
    from pydantic import AfterValidator
    
    app = FastAPI()
    
    data = {
        "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
        "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
        "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
    }
    
    
    def check_valid_id(id: str):
        if not id.startswith(("isbn-", "imdb-")):
            raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
        return id
    
    
    @app.get("/items/")
    async def read_items(
        id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
    ):
        if id:
            item = data.get(id)
        else:
            id, item = random.choice(list(data.items()))
        return {"id": id, "name": item}
    

```

## Резюме

Вы можете объявлять дополнительные проверки и метаданные для параметров.

Общие метаданные и настройки:

  * `alias`
  * `title`
  * `description`
  * `deprecated`

Проверки, специфичные для строк:

  * `min_length`
  * `max_length`
  * `pattern`

Кастомные проверки с использованием `AfterValidator`.

В этих примерах вы видели, как объявлять проверки для значений типа `str`.

Смотрите следующие главы, чтобы узнать, как объявлять проверки для других типов, например чисел.
  *[ISBN]: International Standard Book Number - Международный стандартный книжный номер
  *[IMDB]: Internet Movie Database - Интернетная база данных фильмов: веб‑сайт с информацией о фильмах
