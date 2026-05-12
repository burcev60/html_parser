---
title: Header-параметры
source: https://fastapi.tiangolo.com/ru/tutorial/header-params/
---

# Header-параметры

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/tutorial/header-params/)

Вы можете определить параметры заголовка таким же образом, как вы определяете параметры `Query`, `Path` и `Cookie`.

## Импорт `Header`

Сперва импортируйте `Header`:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Header
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(user_agent: Annotated[str | None, Header()] = None):
        return {"User-Agent": user_agent}
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Header
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(user_agent: str | None = Header(default=None)):
        return {"User-Agent": user_agent}
    

```

## Объявление параметров `Header`

Затем объявите параметры заголовка, используя ту же структуру, что и с `Path`, `Query` и `Cookie`.

Первое значение является значением по умолчанию, вы можете передать все дополнительные параметры валидации или аннотации:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Header
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(user_agent: Annotated[str | None, Header()] = None):
        return {"User-Agent": user_agent}
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Header
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(user_agent: str | None = Header(default=None)):
        return {"User-Agent": user_agent}
    

```

Технические детали

`Header` \- это "родственный" класс `Path`, `Query` и `Cookie`. Он также наследуется от того же общего класса `Param`.

Но помните, что когда вы импортируете `Query`, `Path`, `Header` и другие из `fastapi`, на самом деле это функции, которые возвращают специальные классы.

Информация

Чтобы объявить заголовки, важно использовать `Header`, иначе параметры интерпретируются как query-параметры.

## Автоматическое преобразование

`Header` обладает небольшой дополнительной функциональностью в дополнение к тому, что предоставляют `Path`, `Query` и `Cookie`.

Большинство стандартных заголовков разделены символом "дефис", также известным как "минус" (`-`).

Но переменная вроде `user-agent` недопустима в Python.

По умолчанию `Header` преобразует символы имен параметров из символа подчеркивания (`_`) в дефис (`-`) для извлечения и документирования заголовков.

Кроме того, HTTP-заголовки не чувствительны к регистру, поэтому вы можете объявить их в стандартном стиле Python (также известном как "snake_case").

Таким образом вы можете использовать `user_agent`, как обычно, в коде Python, вместо того, чтобы вводить заглавные буквы как `User_Agent` или что-то подобное.

Если по какой-либо причине вам необходимо отключить автоматическое преобразование подчеркиваний в дефисы, установите для параметра `convert_underscores` в `Header` значение `False`:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Header
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(
        strange_header: Annotated[str | None, Header(convert_underscores=False)] = None,
    ):
        return {"strange_header": strange_header}
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Header
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(
        strange_header: str | None = Header(default=None, convert_underscores=False),
    ):
        return {"strange_header": strange_header}
    

```

Внимание

Прежде чем установить для `convert_underscores` значение `False`, имейте в виду, что некоторые HTTP-прокси и серверы запрещают использование заголовков с подчеркиванием.

## Повторяющиеся заголовки

Есть возможность получать несколько заголовков с одним и тем же именем, но разными значениями.

Вы можете определить эти случаи, используя список в объявлении типа.

Вы получите все значения из повторяющегося заголовка в виде `list` Python.

Например, чтобы объявить заголовок `X-Token`, который может появляться более одного раза, вы можете написать:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import FastAPI, Header
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
        return {"X-Token values": x_token}
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import FastAPI, Header
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(x_token: list[str] | None = Header(default=None)):
        return {"X-Token values": x_token}
    

```

Если вы взаимодействуете с этой _операцией пути_ , отправляя два HTTP-заголовка, таких как:

```
 
    X-Token: foo
    X-Token: bar
    

```

Ответ был бы таким:

```
 
    {
        "X-Token values": [
            "bar",
            "foo"
        ]
    }
    

```

## Резюме

Объявляйте заголовки с помощью `Header`, используя тот же общий шаблон, как при `Query`, `Path` и `Cookie`.

И не беспокойтесь о символах подчеркивания в ваших переменных, **FastAPI** позаботится об их преобразовании.
