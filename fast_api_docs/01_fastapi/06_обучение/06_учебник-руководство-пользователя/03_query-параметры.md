---
title: Query-параметры
source: https://fastapi.tiangolo.com/ru/tutorial/query-params/
---

# Query-параметры

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/tutorial/query-params/)

Когда вы объявляете параметры функции, которые не являются параметрами пути, они автоматически интерпретируются как "query"-параметры.

Python 3.10+

```
 
    from fastapi import FastAPI
    
    app = FastAPI()
    
    fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
    
    
    @app.get("/items/")
    async def read_item(skip: int = 0, limit: int = 10):
        return fake_items_db[skip : skip + limit]
    

```

Query-параметры представляют из себя набор пар ключ-значение, которые идут после знака `?` в URL-адресе, разделенные символами `&`.

Например, в этом URL-адресе:

```
 
    http://127.0.0.1:8000/items/?skip=0&limit=10
    

```

...параметры запроса такие:

  * `skip`: со значением `0`
  * `limit`: со значением `10`

Будучи частью URL-адреса, они "по умолчанию" являются строками.

Но когда вы объявляете их с использованием типов Python (в примере выше, как `int`), они конвертируются в указанный тип данных и проходят проверку на соответствие ему.

Все те же правила, которые применяются к path-параметрам, также применяются и query-параметрам:

  * Поддержка от редактора кода (очевидно)
  * "Парсинг" данных
  * Проверка на соответствие данных (Валидация)
  * Автоматическая документация

## Значения по умолчанию

Поскольку query-параметры не являются фиксированной частью пути, они могут быть не обязательными и иметь значения по умолчанию.

В примере выше значения по умолчанию равны `skip=0` и `limit=10`.

Таким образом, результат перехода по URL-адресу:

```
 
    http://127.0.0.1:8000/items/
    

```

будет таким же, как если перейти используя параметры по умолчанию:

```
 
    http://127.0.0.1:8000/items/?skip=0&limit=10
    

```

Но если вы введёте, например:

```
 
    http://127.0.0.1:8000/items/?skip=20
    

```

Значения параметров в вашей функции будут:

  * `skip=20`: потому что вы установили это в URL-адресе
  * `limit=10`: т.к это было значение по умолчанию

## Необязательные параметры

Аналогично, вы можете объявлять необязательные query-параметры, установив их значение по умолчанию, равное `None`:

Python 3.10+

```
 
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/items/{item_id}")
    async def read_item(item_id: str, q: str | None = None):
        if q:
            return {"item_id": item_id, "q": q}
        return {"item_id": item_id}
    

```

В этом случае, параметр `q` будет не обязательным и будет иметь значение `None` по умолчанию.

Важно

Также обратите внимание, что **FastAPI** достаточно умён чтобы заметить, что параметр `item_id` является path-параметром, а `q` нет, поэтому, это параметр запроса.

## Преобразование типа параметра запроса

Вы также можете объявлять параметры с типом `bool`, которые будут преобразованы соответственно:

Python 3.10+

```
 
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/items/{item_id}")
    async def read_item(item_id: str, q: str | None = None, short: bool = False):
        item = {"item_id": item_id}
        if q:
            item.update({"q": q})
        if not short:
            item.update(
                {"description": "This is an amazing item that has a long description"}
            )
        return item
    

```

В этом случае, если вы сделаете запрос:

```
 
    http://127.0.0.1:8000/items/foo?short=1
    

```

или

```
 
    http://127.0.0.1:8000/items/foo?short=True
    

```

или

```
 
    http://127.0.0.1:8000/items/foo?short=true
    

```

или

```
 
    http://127.0.0.1:8000/items/foo?short=on
    

```

или

```
 
    http://127.0.0.1:8000/items/foo?short=yes
    

```

или в любом другом варианте написания (в верхнем регистре, с заглавной буквой, и т.п), внутри вашей функции параметр `short` будет иметь значение `True` типа данных `bool` . В противном случае - `False`.

## Смешивание query-параметров и path-параметров

Вы можете объявлять несколько query-параметров и path-параметров одновременно, **FastAPI** сам разберётся, что чем является.

И вы не обязаны объявлять их в каком-либо определенном порядке.

Они будут обнаружены по именам:

Python 3.10+

```
 
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/users/{user_id}/items/{item_id}")
    async def read_user_item(
        user_id: int, item_id: str, q: str | None = None, short: bool = False
    ):
        item = {"item_id": item_id, "owner_id": user_id}
        if q:
            item.update({"q": q})
        if not short:
            item.update(
                {"description": "This is an amazing item that has a long description"}
            )
        return item
    

```

## Обязательные query-параметры

Когда вы объявляете значение по умолчанию для параметра, который не является path-параметром (в этом разделе мы пока что рассмотрели только query-параметры), то он не является обязательным.

Если вы не хотите задавать конкретное значение, но хотите сделать параметр необязательным, вы можете установить значение по умолчанию равным `None`.

Но если вы хотите сделать query-параметр обязательным, вы можете просто не указывать значение по умолчанию:

Python 3.10+

```
 
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/items/{item_id}")
    async def read_user_item(item_id: str, needy: str):
        item = {"item_id": item_id, "needy": needy}
        return item
    

```

Здесь параметр запроса `needy` является обязательным параметром с типом данных `str`.

Если вы откроете в браузере URL-адрес, например:

```
 
    http://127.0.0.1:8000/items/foo-item
    

```

...без добавления обязательного параметра `needy`, вы увидите подобного рода ошибку:

```
 
    {
      "detail": [
        {
          "type": "missing",
          "loc": [
            "query",
            "needy"
          ],
          "msg": "Field required",
          "input": null
        }
      ]
    }
    

```

Поскольку `needy` является обязательным параметром, вам необходимо указать его в URL-адресе:

```
 
    http://127.0.0.1:8000/items/foo-item?needy=sooooneedy
    

```

...это будет работать:

```
 
    {
        "item_id": "foo-item",
        "needy": "sooooneedy"
    }
    

```

Конечно, вы можете определить некоторые параметры как обязательные, некоторые — со значением по умолчанию, а некоторые — полностью необязательные:

Python 3.10+

```
 
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/items/{item_id}")
    async def read_user_item(
        item_id: str, needy: str, skip: int = 0, limit: int | None = None
    ):
        item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
        return item
    

```

В этом примере, у нас есть 3 параметра запроса:

  * `needy`, обязательный `str`.
  * `skip`, типа `int` и со значением по умолчанию `0`.
  * `limit`, необязательный `int`.

Подсказка

Вы можете использовать класс `Enum` также, как ранее применяли его с [Path-параметрами](https://fastapi.tiangolo.com/ru/tutorial/path-params/#predefined-values) ([local](./02_path-параметры.md#predefined-values)).
