---
title: События lifespan
source: https://fastapi.tiangolo.com/ru/advanced/events/
---

# События lifespan

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/advanced/events/)

Вы можете определить логику (код), которую нужно выполнить перед тем, как приложение начнет запускаться. Это означает, что этот код будет выполнен один раз, перед тем как приложение начнет получать HTTP-запросы.

Аналогично, вы можете определить логику (код), которую нужно выполнить, когда приложение завершает работу. В этом случае код будет выполнен один раз, после обработки, возможно, многих запросов.

Поскольку этот код выполняется до того, как приложение начинает принимать запросы, и сразу после того, как оно заканчивает их обрабатывать, он охватывает весь lifespan (жизненный цикл) приложения (слово «lifespan» станет важным через секунду 😉).

Это может быть очень полезно для настройки ресурсов, которые нужны для всего приложения, которые разделяются между запросами и/или которые нужно затем очистить. Например, пул подключений к базе данных или загрузка общей модели Машинного обучения.

## Вариант использования

Начнем с примера варианта использования, а затем посмотрим, как это решить.

Представим, что у вас есть несколько моделей Машинного обучения, которые вы хотите использовать для обработки запросов. 🤖

Эти же модели разделяются между запросами, то есть это не одна модель на запрос, не одна на пользователя и т.п.

Представим, что загрузка модели может занимать довольно много времени, потому что ей нужно прочитать много данных с диска. Поэтому вы не хотите делать это для каждого запроса.

Вы могли бы загрузить её на верхнем уровне модуля/файла, но это означало бы, что модель загружается даже если вы просто запускаете простой автоматический тест; тогда этот тест будет медленным, так как ему придется ждать загрузки модели перед запуском независимой части кода.

Именно это мы и решим: давайте загружать модель перед тем, как начнётся обработка запросов, но только непосредственно перед тем, как приложение начнет принимать запросы, а не во время загрузки кода.

## Lifespan

Вы можете определить логику для startup и shutdown, используя параметр `lifespan` приложения `FastAPI` и «менеджер контекста» (через секунду покажу что это).

Начнем с примера, а затем разберём его подробнее.

Мы создаём асинхронную функцию `lifespan()` с `yield` примерно так:

Python 3.10+

```
 
    from contextlib import asynccontextmanager
    
    from fastapi import FastAPI
    
    
    def fake_answer_to_everything_ml_model(x: float):
        return x * 42
    
    
    ml_models = {}
    
    
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        # Load the ML model
        ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
        yield
        # Clean up the ML models and release the resources
        ml_models.clear()
    
    
    app = FastAPI(lifespan=lifespan)
    
    
    @app.get("/predict")
    async def predict(x: float):
        result = ml_models["answer_to_everything"](x)
        return {"result": result}
    

```

Здесь мы симулируем дорогую операцию startup по загрузке модели, помещая (фиктивную) функцию модели в словарь с моделями Машинного обучения до `yield`. Этот код будет выполнен до того, как приложение начнет принимать запросы, во время startup.

А затем сразу после `yield` мы выгружаем модель. Этот код будет выполнен после того, как приложение закончит обрабатывать запросы, непосредственно перед shutdown. Это может, например, освободить ресурсы, такие как память или GPU.

Совет

`shutdown` произойдёт, когда вы останавливаете приложение.

Возможно, вам нужно запустить новую версию, или вы просто устали от него. 🤷

### Функция lifespan

Первое, на что стоит обратить внимание, — мы определяем асинхронную функцию с `yield`. Это очень похоже на Зависимости с `yield`.

Python 3.10+

```
 
    from contextlib import asynccontextmanager
    
    from fastapi import FastAPI
    
    
    def fake_answer_to_everything_ml_model(x: float):
        return x * 42
    
    
    ml_models = {}
    
    
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        # Load the ML model
        ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
        yield
        # Clean up the ML models and release the resources
        ml_models.clear()
    
    
    app = FastAPI(lifespan=lifespan)
    
    
    @app.get("/predict")
    async def predict(x: float):
        result = ml_models["answer_to_everything"](x)
        return {"result": result}
    

```

Первая часть функции, до `yield`, будет выполнена до запуска приложения.

А часть после `yield` будет выполнена после завершения работы приложения.

### Асинхронный менеджер контекста

Если присмотреться, функция декорирована `@asynccontextmanager`.

Это превращает функцию в «асинхронный менеджер контекста».

Python 3.10+

```
 
    from contextlib import asynccontextmanager
    
    from fastapi import FastAPI
    
    
    def fake_answer_to_everything_ml_model(x: float):
        return x * 42
    
    
    ml_models = {}
    
    
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        # Load the ML model
        ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
        yield
        # Clean up the ML models and release the resources
        ml_models.clear()
    
    
    app = FastAPI(lifespan=lifespan)
    
    
    @app.get("/predict")
    async def predict(x: float):
        result = ml_models["answer_to_everything"](x)
        return {"result": result}
    

```

Менеджер контекста в Python — это то, что можно использовать в операторе `with`. Например, `open()` можно использовать как менеджер контекста:

```
 
    with open("file.txt") as file:
        file.read()
    

```

В последних версиях Python есть также асинхронный менеджер контекста. Его используют с `async with`:

```
 
    async with lifespan(app):
        await do_stuff()
    

```

Когда вы создаёте менеджер контекста или асинхронный менеджер контекста, как выше, он перед входом в блок `with` выполнит код до `yield`, а после выхода из блока `with` выполнит код после `yield`.

В нашем примере выше мы не используем его напрямую, а передаём его в FastAPI, чтобы он использовал его сам.

Параметр `lifespan` приложения `FastAPI` принимает асинхронный менеджер контекста, поэтому мы можем передать ему наш новый асинхронный менеджер контекста `lifespan`.

Python 3.10+

```
 
    from contextlib import asynccontextmanager
    
    from fastapi import FastAPI
    
    
    def fake_answer_to_everything_ml_model(x: float):
        return x * 42
    
    
    ml_models = {}
    
    
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        # Load the ML model
        ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
        yield
        # Clean up the ML models and release the resources
        ml_models.clear()
    
    
    app = FastAPI(lifespan=lifespan)
    
    
    @app.get("/predict")
    async def predict(x: float):
        result = ml_models["answer_to_everything"](x)
        return {"result": result}
    

```

## Альтернативные события (устаревшие)

Предупреждение

Рекомендуемый способ обрабатывать startup и shutdown — использовать параметр `lifespan` приложения `FastAPI`, как описано выше. Если вы укажете параметр `lifespan`, обработчики событий `startup` и `shutdown` больше вызываться не будут. Либо всё через `lifespan`, либо всё через события — не одновременно.

Эту часть, скорее всего, можно пропустить.

Есть альтернативный способ определить логику, которую нужно выполнить во время startup и во время shutdown.

Вы можете определить обработчики событий (функции), которые нужно выполнить до старта приложения или при его завершении.

Эти функции можно объявить с `async def` или обычным `def`.

### Событие `startup`

Чтобы добавить функцию, которую нужно запустить до старта приложения, объявите её как обработчик события `"startup"`:

Python 3.10+

```
 
    from fastapi import FastAPI
    
    app = FastAPI()
    
    items = {}
    
    
    @app.on_event("startup")
    async def startup_event():
        items["foo"] = {"name": "Fighters"}
        items["bar"] = {"name": "Tenders"}
    
    
    @app.get("/items/{item_id}")
    async def read_items(item_id: str):
        return items[item_id]
    

```

В этом случае функция-обработчик события `startup` инициализирует «базу данных» items (это просто `dict`) некоторыми значениями.

Вы можете добавить более одного обработчика события.

И ваше приложение не начнет принимать запросы, пока все обработчики события `startup` не завершатся.

### Событие `shutdown`

Чтобы добавить функцию, которую нужно запустить при завершении работы приложения, объявите её как обработчик события `"shutdown"`:

Python 3.10+

```
 
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.on_event("shutdown")
    def shutdown_event():
        with open("log.txt", mode="a") as log:
            log.write("Application shutdown")
    
    
    @app.get("/items/")
    async def read_items():
        return [{"name": "Foo"}]
    

```

Здесь функция-обработчик события `shutdown` запишет строку текста `"Application shutdown"` в файл `log.txt`.

Информация

В функции `open()` параметр `mode="a"` означает «добавление» (append), то есть строка будет добавлена в конец файла, без перезаписи предыдущего содержимого.

Совет

Обратите внимание, что в этом случае мы используем стандартную Python-функцию `open()`, которая взаимодействует с файлом.

То есть это I/O (ввод/вывод), требующий «ожидания» записи на диск.

Но `open()` не использует `async` и `await`.

Поэтому мы объявляем обработчик события обычным `def` вместо `async def`.

### `startup` и `shutdown` вместе

С высокой вероятностью логика для вашего startup и shutdown связана: вы можете хотеть что-то запустить, а затем завершить, получить ресурс, а затем освободить его и т.д.

Делать это в отдельных функциях, которые не разделяют общую логику или переменные, сложнее, так как придётся хранить значения в глобальных переменных или использовать похожие приёмы.

Поэтому теперь рекомендуется использовать `lifespan`, как описано выше.

## Технические детали

Немного технических подробностей для любопытных умников. 🤓

Под капотом, в ASGI-технической спецификации, это часть [Протокола Lifespan](https://asgi.readthedocs.io/en/latest/specs/lifespan.html), и он определяет события `startup` и `shutdown`.

Информация

Вы можете прочитать больше про обработчики `lifespan` в Starlette в [документации Starlette по Lifespan](https://www.starlette.dev/lifespan/).

Включая то, как работать с состоянием lifespan, которое можно использовать в других частях вашего кода.

## Подприложения

🚨 Имейте в виду, что эти события lifespan (startup и shutdown) будут выполнены только для основного приложения, а не для [Подприложения — Mounts](https://fastapi.tiangolo.com/ru/advanced/sub-applications/) ([local](./16_подприложения-mounts-монтирование.md)).
