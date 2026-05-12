---
title: Зависимости с yield
source: https://fastapi.tiangolo.com/ru/tutorial/dependencies/dependencies-with-yield/
---

# Зависимости с yield

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/)

FastAPI поддерживает зависимости, которые выполняют некоторые дополнительные шаги после завершения.

Для этого используйте `yield` вместо `return`, а дополнительные шаги (код) напишите после него.

Подсказка

Убедитесь, что используете `yield` только один раз на одну зависимость.

Технические детали

Любая функция, с которой можно корректно использовать:

  * [`@contextlib.contextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager) или
  * [`@contextlib.asynccontextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.asynccontextmanager)

будет корректной для использования в качестве зависимости **FastAPI**.

На самом деле, FastAPI использует эти два декоратора внутренне.

## Зависимость базы данных с помощью `yield`

Например, с его помощью можно создать сессию работы с базой данных и закрыть её после завершения.

Перед созданием ответа будет выполнен только код до и включая оператор `yield`:

Python 3.10+

```
 
    async def get_db():
        db = DBSession()
        try:
            yield db
        finally:
            db.close()
    

```

Значение, полученное из `yield`, внедряется в _операции пути_ и другие зависимости:

Python 3.10+

```
 
    async def get_db():
        db = DBSession()
        try:
            yield db
        finally:
            db.close()
    

```

Код, следующий за оператором `yield`, выполняется после ответа:

Python 3.10+

```
 
    async def get_db():
        db = DBSession()
        try:
            yield db
        finally:
            db.close()
    

```

Подсказка

Можно использовать как `async`, так и обычные функции.

**FastAPI** корректно обработает каждый вариант, так же как и с обычными зависимостями.

## Зависимость с `yield` и `try`

Если использовать блок `try` в зависимости с `yield`, то вы получите любое исключение, которое было выброшено при использовании зависимости.

Например, если какой-то код в какой-то момент в середине, в другой зависимости или в _операции пути_ , сделал "откат" транзакции базы данных или создал любую другую ошибку, то вы получите это исключение в своей зависимости.

Таким образом, можно искать конкретное исключение внутри зависимости с помощью `except SomeException`.

Точно так же можно использовать `finally`, чтобы убедиться, что обязательные шаги при выходе выполнены независимо от того, было ли исключение или нет.

Python 3.10+

```
 
    async def get_db():
        db = DBSession()
        try:
            yield db
        finally:
            db.close()
    

```

## Подзависимости с `yield`

Вы можете иметь подзависимости и "деревья" подзависимостей любого размера и формы, и любая из них или все они могут использовать `yield`.

**FastAPI** проследит за тем, чтобы «код выхода» в каждой зависимости с `yield` выполнялся в правильном порядке.

Например, `dependency_c` может зависеть от `dependency_b`, а `dependency_b` — от `dependency_a`:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import Depends
    
    
    async def dependency_a():
        dep_a = generate_dep_a()
        try:
            yield dep_a
        finally:
            dep_a.close()
    
    
    async def dependency_b(dep_a: Annotated[DepA, Depends(dependency_a)]):
        dep_b = generate_dep_b()
        try:
            yield dep_b
        finally:
            dep_b.close(dep_a)
    
    
    async def dependency_c(dep_b: Annotated[DepB, Depends(dependency_b)]):
        dep_c = generate_dep_c()
        try:
            yield dep_c
        finally:
            dep_c.close(dep_b)
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import Depends
    
    
    async def dependency_a():
        dep_a = generate_dep_a()
        try:
            yield dep_a
        finally:
            dep_a.close()
    
    
    async def dependency_b(dep_a=Depends(dependency_a)):
        dep_b = generate_dep_b()
        try:
            yield dep_b
        finally:
            dep_b.close(dep_a)
    
    
    async def dependency_c(dep_b=Depends(dependency_b)):
        dep_c = generate_dep_c()
        try:
            yield dep_c
        finally:
            dep_c.close(dep_b)
    

```

И все они могут использовать `yield`.

В этом случае `dependency_c` для выполнения своего кода выхода нуждается в том, чтобы значение из `dependency_b` (здесь `dep_b`) всё ещё было доступно.

И, в свою очередь, `dependency_b` нуждается в том, чтобы значение из `dependency_a` (здесь `dep_a`) было доступно для её кода выхода.

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import Depends
    
    
    async def dependency_a():
        dep_a = generate_dep_a()
        try:
            yield dep_a
        finally:
            dep_a.close()
    
    
    async def dependency_b(dep_a: Annotated[DepA, Depends(dependency_a)]):
        dep_b = generate_dep_b()
        try:
            yield dep_b
        finally:
            dep_b.close(dep_a)
    
    
    async def dependency_c(dep_b: Annotated[DepB, Depends(dependency_b)]):
        dep_c = generate_dep_c()
        try:
            yield dep_c
        finally:
            dep_c.close(dep_b)
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import Depends
    
    
    async def dependency_a():
        dep_a = generate_dep_a()
        try:
            yield dep_a
        finally:
            dep_a.close()
    
    
    async def dependency_b(dep_a=Depends(dependency_a)):
        dep_b = generate_dep_b()
        try:
            yield dep_b
        finally:
            dep_b.close(dep_a)
    
    
    async def dependency_c(dep_b=Depends(dependency_b)):
        dep_c = generate_dep_c()
        try:
            yield dep_c
        finally:
            dep_c.close(dep_b)
    

```

Точно так же можно иметь часть зависимостей с `yield`, часть — с `return`, и какие-то из них могут зависеть друг от друга.

Либо у вас может быть одна зависимость, которая требует несколько других зависимостей с `yield` и т.д.

Комбинации зависимостей могут быть какими угодно.

**FastAPI** проследит за тем, чтобы всё выполнялось в правильном порядке.

Технические детали

Это работает благодаря [менеджерам контекста](https://docs.python.org/3/library/contextlib.html) в Python.

**FastAPI** использует их внутренне для достижения этого.

## Зависимости с `yield` и `HTTPException`

Вы видели, что можно использовать зависимости с `yield` и иметь блоки `try`, которые пытаются выполнить некоторый код, а затем запускают код выхода в `finally`.

Также вы можете использовать `except`, чтобы поймать вызванное исключение и что-то с ним сделать.

Например, вы можете вызвать другое исключение, например `HTTPException`.

Подсказка

Это довольно продвинутая техника, и в большинстве случаев она вам не понадобится, так как вы можете вызывать исключения (включая `HTTPException`) в остальном коде вашего приложения, например, в _функции-обработчике пути_.

Но если понадобится — возможность есть. 🤓

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import Depends, FastAPI, HTTPException
    
    app = FastAPI()
    
    
    data = {
        "plumbus": {"description": "Freshly pickled plumbus", "owner": "Morty"},
        "portal-gun": {"description": "Gun to create portals", "owner": "Rick"},
    }
    
    
    class OwnerError(Exception):
        pass
    
    
    def get_username():
        try:
            yield "Rick"
        except OwnerError as e:
            raise HTTPException(status_code=400, detail=f"Owner error: {e}")
    
    
    @app.get("/items/{item_id}")
    def get_item(item_id: str, username: Annotated[str, Depends(get_username)]):
        if item_id not in data:
            raise HTTPException(status_code=404, detail="Item not found")
        item = data[item_id]
        if item["owner"] != username:
            raise OwnerError(username)
        return item
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import Depends, FastAPI, HTTPException
    
    app = FastAPI()
    
    
    data = {
        "plumbus": {"description": "Freshly pickled plumbus", "owner": "Morty"},
        "portal-gun": {"description": "Gun to create portals", "owner": "Rick"},
    }
    
    
    class OwnerError(Exception):
        pass
    
    
    def get_username():
        try:
            yield "Rick"
        except OwnerError as e:
            raise HTTPException(status_code=400, detail=f"Owner error: {e}")
    
    
    @app.get("/items/{item_id}")
    def get_item(item_id: str, username: str = Depends(get_username)):
        if item_id not in data:
            raise HTTPException(status_code=404, detail="Item not found")
        item = data[item_id]
        if item["owner"] != username:
            raise OwnerError(username)
        return item
    

```

Если вы хотите перехватывать исключения и формировать на их основе пользовательский ответ, создайте [Пользовательский обработчик исключений](https://fastapi.tiangolo.com/ru/tutorial/handling-errors/#install-custom-exception-handlers) ([local](./../24_обработка-ошибок.md#install-custom-exception-handlers)).

## Зависимости с `yield` и `except`

Если вы ловите исключение с помощью `except` в зависимости с `yield` и не вызываете его снова (или не вызываете новое исключение), FastAPI не сможет заметить, что было исключение — так же, как это происходит в обычном Python:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import Depends, FastAPI, HTTPException
    
    app = FastAPI()
    
    
    class InternalError(Exception):
        pass
    
    
    def get_username():
        try:
            yield "Rick"
        except InternalError:
            print("Oops, we didn't raise again, Britney 😱")
    
    
    @app.get("/items/{item_id}")
    def get_item(item_id: str, username: Annotated[str, Depends(get_username)]):
        if item_id == "portal-gun":
            raise InternalError(
                f"The portal gun is too dangerous to be owned by {username}"
            )
        if item_id != "plumbus":
            raise HTTPException(
                status_code=404, detail="Item not found, there's only a plumbus here"
            )
        return item_id
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import Depends, FastAPI, HTTPException
    
    app = FastAPI()
    
    
    class InternalError(Exception):
        pass
    
    
    def get_username():
        try:
            yield "Rick"
        except InternalError:
            print("Oops, we didn't raise again, Britney 😱")
    
    
    @app.get("/items/{item_id}")
    def get_item(item_id: str, username: str = Depends(get_username)):
        if item_id == "portal-gun":
            raise InternalError(
                f"The portal gun is too dangerous to be owned by {username}"
            )
        if item_id != "plumbus":
            raise HTTPException(
                status_code=404, detail="Item not found, there's only a plumbus here"
            )
        return item_id
    

```

В этом случае клиент получит _HTTP 500 Internal Server Error_ , как и должно быть, поскольку мы не вызываем `HTTPException` или что-то подобное, но на сервере **не будет никаких логов** или других указаний на то, какая была ошибка. 😱

### Всегда делайте `raise` в зависимостях с `yield` и `except`

Если вы ловите исключение в зависимости с `yield`, то, если вы не вызываете другой `HTTPException` или что-то подобное, вам следует повторно вызвать исходное исключение.

Вы можете повторно вызвать то же самое исключение с помощью `raise`:

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import Depends, FastAPI, HTTPException
    
    app = FastAPI()
    
    
    class InternalError(Exception):
        pass
    
    
    def get_username():
        try:
            yield "Rick"
        except InternalError:
            print("We don't swallow the internal error here, we raise again 😎")
            raise
    
    
    @app.get("/items/{item_id}")
    def get_item(item_id: str, username: Annotated[str, Depends(get_username)]):
        if item_id == "portal-gun":
            raise InternalError(
                f"The portal gun is too dangerous to be owned by {username}"
            )
        if item_id != "plumbus":
            raise HTTPException(
                status_code=404, detail="Item not found, there's only a plumbus here"
            )
        return item_id
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import Depends, FastAPI, HTTPException
    
    app = FastAPI()
    
    
    class InternalError(Exception):
        pass
    
    
    def get_username():
        try:
            yield "Rick"
        except InternalError:
            print("We don't swallow the internal error here, we raise again 😎")
            raise
    
    
    @app.get("/items/{item_id}")
    def get_item(item_id: str, username: str = Depends(get_username)):
        if item_id == "portal-gun":
            raise InternalError(
                f"The portal gun is too dangerous to be owned by {username}"
            )
        if item_id != "plumbus":
            raise HTTPException(
                status_code=404, detail="Item not found, there's only a plumbus here"
            )
        return item_id
    

```

Теперь клиент получит тот же _HTTP 500 Internal Server Error_ , но на сервере в логах будет наше пользовательское `InternalError`. 😎

## Выполнение зависимостей с `yield`

Последовательность выполнения примерно такая, как на этой схеме. Время течёт сверху вниз. А каждый столбец — это одна из частей, взаимодействующих с кодом или выполняющих код.

```
 
    sequenceDiagram
    
    participant client as Client
    participant handler as Exception handler
    participant dep as Dep with yield
    participant operation as Path Operation
    participant tasks as Background tasks
    
        Note over client,operation: Can raise exceptions, including HTTPException
        client ->> dep: Start request
        Note over dep: Run code up to yield
        opt raise Exception
            dep -->> handler: Raise Exception
            handler -->> client: HTTP error response
        end
        dep ->> operation: Run dependency, e.g. DB session
        opt raise
            operation -->> dep: Raise Exception (e.g. HTTPException)
            opt handle
                dep -->> dep: Can catch exception, raise a new HTTPException, raise other exception
            end
            handler -->> client: HTTP error response
        end
    
        operation ->> client: Return response to client
        Note over client,operation: Response is already sent, can't change it anymore
        opt Tasks
            operation -->> tasks: Send background tasks
        end
        opt Raise other exception
            tasks -->> tasks: Handle exceptions in the background task code
        end

```

Дополнительная информация

Клиенту будет отправлен только **один ответ**. Это может быть один из ответов об ошибке или ответ от _операции пути_.

После отправки одного из этих ответов никакой другой ответ отправить нельзя.

Подсказка

Если вы вызовете какое-либо исключение в коде из _функции-обработчика пути_ , оно будет передано зависимостям с `yield`, включая `HTTPException`. В большинстве случаев вы захотите повторно вызвать то же самое исключение или новое из зависимости с `yield`, чтобы убедиться, что оно корректно обработано.

## Ранний выход и `scope`

Обычно «код выхода» зависимостей с `yield` выполняется **после того, как ответ** отправлен клиенту.

Но если вы знаете, что не будете использовать зависимость после возврата из _функции-обработчика пути_ , вы можете использовать `Depends(scope="function")`, чтобы сообщить FastAPI, что он должен закрыть зависимость после возврата из _функции-обработчика пути_ , но **до того** , как **ответ будет отправлен**.

Python 3.10+

```
 
    from typing import Annotated
    
    from fastapi import Depends, FastAPI
    
    app = FastAPI()
    
    
    def get_username():
        try:
            yield "Rick"
        finally:
            print("Cleanup up before response is sent")
    
    
    @app.get("/users/me")
    def get_user_me(username: Annotated[str, Depends(get_username, scope="function")]):
        return username
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from fastapi import Depends, FastAPI
    
    app = FastAPI()
    
    
    def get_username():
        try:
            yield "Rick"
        finally:
            print("Cleanup up before response is sent")
    
    
    @app.get("/users/me")
    def get_user_me(username: str = Depends(get_username, scope="function")):
        return username
    

```

`Depends()` принимает параметр `scope`, который может быть:

  * `"function"`: начать зависимость до _функции-обработчика пути_ , которая обрабатывает запрос, завершить зависимость после окончания _функции-обработчика пути_ , но **до того** , как ответ будет отправлен обратно клиенту. То есть функция зависимости будет выполнена **вокруг** _функции-обработчика пути_.
  * `"request"`: начать зависимость до _функции-обработчика пути_ , которая обрабатывает запрос (как и при использовании `"function"`), но завершить **после** того, как ответ будет отправлен обратно клиенту. То есть функция зависимости будет выполнена **вокруг** цикла запроса (**request**) и ответа.

Если не указано и в зависимости есть `yield`, по умолчанию будет `scope` со значением `"request"`.

### `scope` для подзависимостей

Когда вы объявляете зависимость с `scope="request"` (значение по умолчанию), любая подзависимость также должна иметь `scope` равный `"request"`.

Но зависимость со `scope` равным `"function"` может иметь зависимости со `scope` `"function"` и со `scope` `"request"`.

Это потому, что любая зависимость должна иметь возможность выполнить свой код выхода раньше подзависимостей, так как ей может понадобиться использовать их во время своего кода выхода.

```
 
    sequenceDiagram
    
    participant client as Client
    participant dep_req as Зависимость scope="request"
    participant dep_func as Зависимость scope="function"
    participant operation as Функция-обработчик пути
    
        client ->> dep_req: Запрос
        Note over dep_req: Выполнить код до yield
        dep_req ->> dep_func: Передать значение
        Note over dep_func: Выполнить код до yield
        dep_func ->> operation: Выполнить функцию-обработчик пути
        operation ->> dep_func: Выход из функции-обработчика пути
        Note over dep_func: Выполнить код после yield
        Note over dep_func: ✅ Зависимость закрыта
        dep_func ->> client: Отправить ответ клиенту
        Note over client: Ответ отправлен
        Note over dep_req: Выполнить код после yield
        Note over dep_req: ✅ Зависимость закрыта

```

## Зависимости с `yield`, `HTTPException`, `except` и фоновыми задачами

Зависимости с `yield` со временем эволюционировали, чтобы покрыть разные сценарии и исправить некоторые проблемы.

Если вы хотите посмотреть, что менялось в разных версиях FastAPI, вы можете прочитать об этом подробнее в продвинутом руководстве: [Продвинутые зависимости — зависимости с `yield`, `HTTPException`, `except` и фоновыми задачами](https://fastapi.tiangolo.com/ru/advanced/advanced-dependencies/#dependencies-with-yield-httpexception-except-and-background-tasks) ([local](./../../08_расширенное-руководство-пользователя/10_продвинутые-зависимости.md#dependencies-with-yield-httpexception-except-and-background-tasks)).

## Контекстные менеджеры

### Что такое «контекстные менеджеры»

«Контекстные менеджеры» — это любые объекты Python, которые можно использовать в операторе `with`.

Например, [можно использовать `with` для чтения файла](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files):

```
 
    with open("./somefile.txt") as f:
        contents = f.read()
        print(contents)
    

```

Под капотом вызов `open("./somefile.txt")` создаёт объект, называемый «контекстным менеджером».

Когда блок `with` завершается, он обязательно закрывает файл, даже если были исключения.

Когда вы создаёте зависимость с `yield`, **FastAPI** внутренне создаёт для неё менеджер контекста и сочетает его с некоторыми другими связанными инструментами.

### Использование менеджеров контекста в зависимостях с `yield`

Внимание

Это, более или менее, «продвинутая» идея.

Если вы только начинаете работать с **FastAPI** , то лучше пока пропустить этот пункт.

В Python можно создавать менеджеры контекста, [создав класс с двумя методами: `__enter__()` и `__exit__()`](https://docs.python.org/3/reference/datamodel.html#context-managers).

Их также можно использовать внутри зависимостей **FastAPI** с `yield`, применяя операторы `with` или `async with` внутри функции зависимости:

Python 3.10+

```
 
    class MySuperContextManager:
        def __init__(self):
            self.db = DBSession()
    
        def __enter__(self):
            return self.db
    
        def __exit__(self, exc_type, exc_value, traceback):
            self.db.close()
    
    
    async def get_db():
        with MySuperContextManager() as db:
            yield db
    

```

Подсказка

Другой способ создания менеджера контекста — с помощью:

  * [`@contextlib.contextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager) или
  * [`@contextlib.asynccontextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.asynccontextmanager)

оформив ими функцию с одним `yield`.

Именно это **FastAPI** использует внутренне для зависимостей с `yield`.

Но использовать эти декораторы для зависимостей FastAPI не обязательно (и не стоит).

FastAPI сделает это за вас на внутреннем уровне.
  *[вызвать]: «raise» дословно - «поднять», но «вызвать», «сгенерировать» или «выбросить» употребляется чаще
