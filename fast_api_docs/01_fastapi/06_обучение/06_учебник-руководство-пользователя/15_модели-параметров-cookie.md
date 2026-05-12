---
title: Модели параметров cookie
source: https://fastapi.tiangolo.com/ru/tutorial/cookie-param-models/
---

# Модели параметров cookie

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/tutorial/cookie-param-models/)

Если у вас есть группа **cookies** , которые связаны между собой, вы можете создать **Pydantic-модель** для их объявления. 🍪

Это позволит вам **переиспользовать модель** в **разных местах** , а также объявить проверки и метаданные сразу для всех параметров. 😎

Заметка

Этот функционал доступен с версии `0.115.0`. 🤓

Совет

Такой же подход применяется для `Query`, `Cookie`, и `Header`. 😎

## Pydantic-модель для cookies

Объявите параметры **cookie** , которые вам нужны, в **Pydantic-модели** , а затем объявите параметр как `Cookie`:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import Cookie, FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Cookies(BaseModel):
        session_id: str
        fatebook_tracker: str | None = None
        googall_tracker: str | None = None
    
    
    @app.get("/items/")
    async def read_items(cookies: Annotated[Cookies, Cookie()]):
        return cookies
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import Cookie, FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Cookies(BaseModel):
        session_id: str
        fatebook_tracker: str | None = None
        googall_tracker: str | None = None
    
    
    @app.get("/items/")
    async def read_items(cookies: Cookies = Cookie()):
        return cookies
    

```

**FastAPI** **извлечёт** данные для **каждого поля** из **cookies** , полученных в запросе, и выдаст вам объявленную Pydantic-модель.

## Проверка сгенерированной документации

Вы можете посмотреть объявленные cookies в графическом интерфейсе Документации по пути `/docs`:

![](https://fastapi.tiangolo.com/img/tutorial/cookie-param-models/image01.png)

Дополнительная информация

Имейте в виду, что, поскольку **браузеры обрабатывают cookies** особым образом и под капотом, они **не** позволят **JavaScript** легко получить доступ к ним.

Если вы перейдёте к **графическому интерфейсу документации API** по пути `/docs`, то сможете увидеть **документацию** по cookies для ваших _операций путей_.

Но даже если вы **заполните данные** и нажмёте "Execute", поскольку графический интерфейс Документации работает с **JavaScript** , cookies не будут отправлены, и вы увидите сообщение об **ошибке** как будто не указывали никаких значений.

## Запрет дополнительных cookies

В некоторых случаях (не особо часто встречающихся) вам может понадобиться **ограничить** cookies, которые вы хотите получать.

Теперь у вашего API есть возможность контролировать своё согласие на использование cookie. 🤪🍪

Вы можете сконфигурировать Pydantic-модель так, чтобы запретить (`forbid`) любые дополнительные (`extra`) поля:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import Cookie, FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Cookies(BaseModel):
        model_config = {"extra": "forbid"}
    
        session_id: str
        fatebook_tracker: str | None = None
        googall_tracker: str | None = None
    
    
    @app.get("/items/")
    async def read_items(cookies: Annotated[Cookies, Cookie()]):
        return cookies
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import Cookie, FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Cookies(BaseModel):
        model_config = {"extra": "forbid"}
    
        session_id: str
        fatebook_tracker: str | None = None
        googall_tracker: str | None = None
    
    
    @app.get("/items/")
    async def read_items(cookies: Cookies = Cookie()):
        return cookies
    

```

Если клиент попробует отправить **дополнительные cookies** , то в ответ он получит **ошибку**.

Бедные баннеры cookies, они всеми силами пытаются получить ваше согласие — и всё ради того, чтобы API его отклонил. 🍪

Например, если клиент попытается отправить cookie `santa_tracker` со значением `good-list-please`, то в ответ он получит **ошибку** , сообщающую ему, что `santa_tracker` cookie не разрешён:

```
 
    {
        "detail": [
            {
                "type": "extra_forbidden",
                "loc": ["cookie", "santa_tracker"],
                "msg": "Extra inputs are not permitted",
                "input": "good-list-please",
            }
        ]
    }
    

```

## Заключение

Вы можете использовать **Pydantic-модели** для объявления **cookies** в **FastAPI**. 😎
