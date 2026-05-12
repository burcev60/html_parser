---
title: Параметры Cookie
source: https://fastapi.tiangolo.com/ru/tutorial/cookie-params/
---

# Параметры Cookie

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/tutorial/cookie-params/)

Вы можете задать параметры Cookie таким же способом, как `Query` и `Path` параметры.

## Импорт `Cookie`

Сначала импортируйте `Cookie`:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import Cookie, FastAPI
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
        return {"ads_id": ads_id}
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import Cookie, FastAPI
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(ads_id: str | None = Cookie(default=None)):
        return {"ads_id": ads_id}
    

```

## Объявление параметров `Cookie`

Затем объявляйте параметры cookie, используя ту же структуру, что и с `Path` и `Query`.

Вы можете задать значение по умолчанию, а также все дополнительные параметры валидации или аннотации:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import Cookie, FastAPI
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
        return {"ads_id": ads_id}
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import Cookie, FastAPI
    
    app = FastAPI()
    
    
    @app.get("/items/")
    async def read_items(ads_id: str | None = Cookie(default=None)):
        return {"ads_id": ads_id}
    

```

Технические детали

`Cookie` \- это класс, родственный `Path` и `Query`. Он также наследуется от общего класса `Param`.

Но помните, что когда вы импортируете `Query`, `Path`, `Cookie` и другое из `fastapi`, это фактически функции, которые возвращают специальные классы.

Дополнительная информация

Для объявления cookies, вам нужно использовать `Cookie`, иначе параметры будут интерпретированы как параметры запроса.

Дополнительная информация

Имейте в виду, что, поскольку **браузеры обрабатывают cookies** особым образом и «за кулисами», они **не** позволяют **JavaScript** просто так получать к ним доступ.

Если вы откроете **интерфейс документации API** на `/docs`, вы сможете увидеть **документацию** по cookies для ваших _операции пути_.

Но даже если вы **заполните данные** и нажмёте «Execute», поскольку UI документации работает с **JavaScript** , cookies отправлены не будут, и вы увидите сообщение об **ошибке** , как будто вы не указали никаких значений.

## Резюме

Объявляйте cookies с помощью `Cookie`, используя тот же общий шаблон, что и `Query`, и `Path`.
