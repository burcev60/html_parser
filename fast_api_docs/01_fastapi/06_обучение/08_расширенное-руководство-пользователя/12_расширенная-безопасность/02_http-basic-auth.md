---
title: HTTP Basic Auth
source: https://fastapi.tiangolo.com/ru/advanced/security/http-basic-auth/
---

# HTTP Basic Auth

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/advanced/security/http-basic-auth/)

Для самых простых случаев можно использовать HTTP Basic Auth.

При HTTP Basic Auth приложение ожидает HTTP-заголовок, который содержит имя пользователя и пароль.

Если его нет, возвращается ошибка HTTP 401 «Unauthorized».

Также возвращается заголовок `WWW-Authenticate` со значением `Basic` и необязательным параметром `realm`.

Это говорит браузеру показать встроенное окно запроса имени пользователя и пароля.

Затем, когда вы вводите эти данные, браузер автоматически отправляет их в заголовке.

## Простой HTTP Basic Auth

  * Импортируйте `HTTPBasic` и `HTTPBasicCredentials`.
  * Создайте «схему» `security` с помощью `HTTPBasic`.
  * Используйте эту `security` как зависимость в вашей _операции пути_.
  * Она возвращает объект типа `HTTPBasicCredentials`:
    * Он содержит отправленные `username` и `password`.

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import Depends, FastAPI
    from fastapi.security import HTTPBasic, HTTPBasicCredentials
    
    app = FastAPI()
    
    security = HTTPBasic()
    
    
    @app.get("/users/me")
    def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
        return {"username": credentials.username, "password": credentials.password}
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import Depends, FastAPI
    from fastapi.security import HTTPBasic, HTTPBasicCredentials
    
    app = FastAPI()
    
    security = HTTPBasic()
    
    
    @app.get("/users/me")
    def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
        return {"username": credentials.username, "password": credentials.password}
    

```

Когда вы впервые откроете URL (или нажмёте кнопку «Execute» в документации), браузер попросит ввести имя пользователя и пароль:

![](https://fastapi.tiangolo.com/img/tutorial/security/image12.png)

## Проверка имени пользователя

Вот более полный пример.

Используйте зависимость, чтобы проверить, корректны ли имя пользователя и пароль.

Для этого используйте стандартный модуль Python [`secrets`](https://docs.python.org/3/library/secrets.html) для проверки имени пользователя и пароля.

`secrets.compare_digest()` должен получать `bytes` или `str`, который содержит только символы ASCII (английские символы). Это значит, что он не будет работать с символами вроде `á`, как в `Sebastián`.

Чтобы это обработать, сначала преобразуем `username` и `password` в `bytes`, закодировав их в UTF-8.

Затем можно использовать `secrets.compare_digest()`, чтобы убедиться, что `credentials.username` равен `"stanleyjobson"`, а `credentials.password` — `"swordfish"`.

Python 3.10+

```
 
    import secrets
    from typing import Annotated
    
    from fastapi import Depends, FastAPI, HTTPException, status
    from fastapi.security import HTTPBasic, HTTPBasicCredentials
    
    app = FastAPI()
    
    security = HTTPBasic()
    
    
    def get_current_username(
        credentials: Annotated[HTTPBasicCredentials, Depends(security)],
    ):
        current_username_bytes = credentials.username.encode("utf8")
        correct_username_bytes = b"stanleyjobson"
        is_correct_username = secrets.compare_digest(
            current_username_bytes, correct_username_bytes
        )
        current_password_bytes = credentials.password.encode("utf8")
        correct_password_bytes = b"swordfish"
        is_correct_password = secrets.compare_digest(
            current_password_bytes, correct_password_bytes
        )
        if not (is_correct_username and is_correct_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
        return credentials.username
    
    
    @app.get("/users/me")
    def read_current_user(username: Annotated[str, Depends(get_current_username)]):
        return {"username": username}
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    import secrets
    
    from fastapi import Depends, FastAPI, HTTPException, status
    from fastapi.security import HTTPBasic, HTTPBasicCredentials
    
    app = FastAPI()
    
    security = HTTPBasic()
    
    
    def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
        current_username_bytes = credentials.username.encode("utf8")
        correct_username_bytes = b"stanleyjobson"
        is_correct_username = secrets.compare_digest(
            current_username_bytes, correct_username_bytes
        )
        current_password_bytes = credentials.password.encode("utf8")
        correct_password_bytes = b"swordfish"
        is_correct_password = secrets.compare_digest(
            current_password_bytes, correct_password_bytes
        )
        if not (is_correct_username and is_correct_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
        return credentials.username
    
    
    @app.get("/users/me")
    def read_current_user(username: str = Depends(get_current_username)):
        return {"username": username}
    

```

Это было бы похоже на:

```
 
    if not (credentials.username == "stanleyjobson") or not (credentials.password == "swordfish"):
        # Вернуть ошибку
        ...
    

```

Но используя `secrets.compare_digest()`, вы защитите код от атак типа «тайминговая атака» (атака по времени).

### Тайминговые атаки

Что такое «тайминговая атака»?

Представим, что злоумышленники пытаются угадать имя пользователя и пароль.

И они отправляют запрос с именем пользователя `johndoe` и паролем `love123`.

Тогда Python-код в вашем приложении будет эквивалентен чему-то вроде:

```
 
    if "johndoe" == "stanleyjobson" and "love123" == "swordfish":
        ...
    

```

Но в момент, когда Python сравнит первую `j` в `johndoe` с первой `s` в `stanleyjobson`, он вернёт `False`, потому что уже ясно, что строки не совпадают, решив, что «нет смысла тратить ресурсы на сравнение остальных букв». И ваше приложение ответит «Неверное имя пользователя или пароль».

Затем злоумышленники попробуют имя пользователя `stanleyjobsox` и пароль `love123`.

И ваш код сделает что-то вроде:

```
 
    if "stanleyjobsox" == "stanleyjobson" and "love123" == "swordfish":
        ...
    

```

Pythonу придётся сравнить весь общий префикс `stanleyjobso` в `stanleyjobsox` и `stanleyjobson`, прежде чем понять, что строки отличаются. Поэтому на ответ «Неверное имя пользователя или пароль» уйдёт на несколько микросекунд больше.

#### Время ответа помогает злоумышленникам

Замечая, что сервер прислал «Неверное имя пользователя или пароль» на несколько микросекунд позже, злоумышленники поймут, что какая-то часть была угадана — начальные буквы верны.

Тогда они могут попробовать снова, зная, что правильнее что-то ближе к `stanleyjobsox`, чем к `johndoe`.

#### «Профессиональная» атака

Конечно, злоумышленники не будут делать всё это вручную — они напишут программу, возможно, с тысячами или миллионами попыток в секунду. И будут подбирать по одной дополнительной верной букве за раз.

Так за минуты или часы они смогут угадать правильные имя пользователя и пароль — с «помощью» нашего приложения — используя лишь время, затраченное на ответ.

#### Исправление с помощью `secrets.compare_digest()`

Но в нашем коде мы используем `secrets.compare_digest()`.

Вкратце: сравнение `stanleyjobsox` с `stanleyjobson` займёт столько же времени, сколько и сравнение `johndoe` с `stanleyjobson`. То же относится и к паролю.

Таким образом, используя `secrets.compare_digest()` в коде приложения, вы защитите его от всего этого класса атак на безопасность.

### Возврат ошибки

После того как обнаружено, что учётные данные некорректны, верните `HTTPException` со статус-кодом ответа 401 (тем же, что и при отсутствии учётных данных) и добавьте HTTP-заголовок `WWW-Authenticate`, чтобы браузер снова показал окно входа:

Python 3.10+

```
 
    import secrets
    from typing import Annotated
    
    from fastapi import Depends, FastAPI, HTTPException, status
    from fastapi.security import HTTPBasic, HTTPBasicCredentials
    
    app = FastAPI()
    
    security = HTTPBasic()
    
    
    def get_current_username(
        credentials: Annotated[HTTPBasicCredentials, Depends(security)],
    ):
        current_username_bytes = credentials.username.encode("utf8")
        correct_username_bytes = b"stanleyjobson"
        is_correct_username = secrets.compare_digest(
            current_username_bytes, correct_username_bytes
        )
        current_password_bytes = credentials.password.encode("utf8")
        correct_password_bytes = b"swordfish"
        is_correct_password = secrets.compare_digest(
            current_password_bytes, correct_password_bytes
        )
        if not (is_correct_username and is_correct_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
        return credentials.username
    
    
    @app.get("/users/me")
    def read_current_user(username: Annotated[str, Depends(get_current_username)]):
        return {"username": username}
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    import secrets
    
    from fastapi import Depends, FastAPI, HTTPException, status
    from fastapi.security import HTTPBasic, HTTPBasicCredentials
    
    app = FastAPI()
    
    security = HTTPBasic()
    
    
    def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
        current_username_bytes = credentials.username.encode("utf8")
        correct_username_bytes = b"stanleyjobson"
        is_correct_username = secrets.compare_digest(
            current_username_bytes, correct_username_bytes
        )
        current_password_bytes = credentials.password.encode("utf8")
        correct_password_bytes = b"swordfish"
        is_correct_password = secrets.compare_digest(
            current_password_bytes, correct_password_bytes
        )
        if not (is_correct_username and is_correct_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
        return credentials.username
    
    
    @app.get("/users/me")
    def read_current_user(username: str = Depends(get_current_username)):
        return {"username": username}
    

```
