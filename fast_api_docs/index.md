---
title: FastAPI
source: https://fastapi.tiangolo.com/ru/
---

# FastAPI

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./01_fastapi/11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/)

[![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)](https://fastapi.tiangolo.com/ru)

_Фреймворк FastAPI: высокая производительность, прост в изучении, позволяет быстро писать код, готов к продакшн_

[ ![Тест](https://github.com/fastapi/fastapi/actions/workflows/test.yml/badge.svg?event=push&branch=master) ](https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster) [ ![Покрытие](https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg) ](https://coverage-badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi) [ ![Версия пакета](https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package) ](https://pypi.org/project/fastapi) [ ![Поддерживаемые версии Python](https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058) ](https://pypi.org/project/fastapi)

* * *

**Документация** : https://fastapi.tiangolo.com

**Исходный код** : <https://github.com/fastapi/fastapi>

* * *

FastAPI — это современный, быстрый (высокопроизводительный) веб-фреймворк для создания API на Python, основанный на стандартных аннотациях типов Python.

Ключевые особенности:

  * **Скорость** : Очень высокая производительность, на уровне **NodeJS** и **Go** (благодаря Starlette и Pydantic). [Один из самых быстрых доступных фреймворков Python](#performance).
  * **Быстрота разработки** : Увеличьте скорость разработки фич примерно на 200–300%. *
  * **Меньше ошибок** : Сократите примерно на 40% количество ошибок, вызванных человеком (разработчиком). *
  * **Интуитивность** : Отличная поддержка редактора кода. Автозавершение везде. Меньше времени на отладку.
  * **Простота** : Разработан так, чтобы его было легко использовать и осваивать. Меньше времени на чтение документации.
  * **Краткость** : Минимизируйте дублирование кода. Несколько возможностей из каждого объявления параметров. Меньше ошибок.
  * **Надежность** : Получите код, готовый к продакшн. С автоматической интерактивной документацией.
  * **На основе стандартов** : Основан на открытых стандартах API и полностью совместим с ними: [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (ранее известный как Swagger) и [JSON Schema](https://json-schema.org/).

* оценка на основе тестов внутренней команды разработчиков, создающих продакшн-приложения.

## Спонсоры

### Ключевой-спонсор

[![](https://fastapi.tiangolo.com/img/sponsors/fastapicloud.png)](https://fastapicloud.com "FastAPI Cloud. By the same team behind FastAPI. You code. We Cloud.")

### Золотые и серебряные спонсоры

[![](https://fastapi.tiangolo.com/img/sponsors/blockbee.png)](https://blockbee.io?ref=fastapi "BlockBee Cryptocurrency Payment Gateway") [![](https://fastapi.tiangolo.com/img/sponsors/scalar.svg)](https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=main-badge "Scalar: Beautiful Open-Source API References from Swagger/OpenAPI files") [![](https://fastapi.tiangolo.com/img/sponsors/propelauth.png)](https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=mainbadge "Auth, user management and more for your B2B product") [![](https://fastapi.tiangolo.com/img/sponsors/liblab.png)](https://liblab.com?utm_source=fastapi "liblab - Generate SDKs from FastAPI") [![](https://fastapi.tiangolo.com/img/sponsors/render.svg)](https://docs.render.com/deploy-fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi "Deploy & scale any full-stack web app on Render. Focus on building apps, not infra.") [![](https://fastapi.tiangolo.com/img/sponsors/coderabbit.png)](https://www.coderabbit.ai/?utm_source=fastapi&utm_medium=badge&utm_campaign=fastapi "Cut Code Review Time & Bugs in Half with CodeRabbit") [![](https://fastapi.tiangolo.com/img/sponsors/subtotal.svg)](https://subtotal.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=open-source "The Gold Standard in Retail Account Linking") [![](https://fastapi.tiangolo.com/img/sponsors/railway.png)](https://docs.railway.com/guides/fastapi?utm_medium=integration&utm_source=docs&utm_campaign=fastapi "Deploy enterprise applications at startup speed") [![](https://fastapi.tiangolo.com/img/sponsors/serpapi.png)](https://serpapi.com/?utm_source=fastapi_website "SerpApi: Web Search API") [![](https://fastapi.tiangolo.com/img/sponsors/greptile.png)](https://www.greptile.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=fastapi_sponsor_page "Greptile: The AI Code Reviewer") [![](https://fastapi.tiangolo.com/img/sponsors/databento.svg)](https://databento.com/?utm_source=fastapi&utm_medium=sponsor&utm_content=display "Pay as you go for market data") [![](https://fastapi.tiangolo.com/img/sponsors/svix.svg)](https://www.svix.com/ "Svix - Webhooks as a service") [![](https://fastapi.tiangolo.com/img/sponsors/stainless.png)](https://www.stainlessapi.com/?utm_source=fastapi&utm_medium=referral "Stainless | Generate best-in-class SDKs") [![](https://fastapi.tiangolo.com/img/sponsors/permit.png)](https://www.permit.io/blog/implement-authorization-in-fastapi?utm_source=github&utm_medium=referral&utm_campaign=fastapi "Fine-Grained Authorization for FastAPI") [![](https://fastapi.tiangolo.com/img/sponsors/interviewpal.png)](https://www.interviewpal.com/?utm_source=fastapi&utm_medium=open-source&utm_campaign=dev-hiring "InterviewPal - AI Interview Coach for Engineers and Devs") [![](https://fastapi.tiangolo.com/img/sponsors/dribia.png)](https://dribia.com/en/ "Dribia - Data Science within your reach")

[Другие спонсоры](https://fastapi.tiangolo.com/ru/fastapi-people/#sponsors) ([local](./01_fastapi/09_fastapi-people.md#sponsors))

## Мнения

"_[...] В последнее время я много где использую**FastAPI**. [...] На самом деле я планирую использовать его для всех **ML-сервисов моей команды в Microsoft**. Некоторые из них интегрируются в основной продукт **Windows** , а некоторые — в продукты **Office**._"

Kabir Khan - **Microsoft** [(ref)](https://github.com/fastapi/fastapi/pull/26)

* * *

"_Мы начали использовать библиотеку**FastAPI** , чтобы поднять **REST** -сервер, к которому можно обращаться за **предсказаниями**. [для Ludwig]_"

Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - **Uber** [(ref)](https://eng.uber.com/ludwig-v0-2/)

* * *

"_**Netflix** рада объявить об открытом релизе нашего фреймворка оркестрации **антикризисного управления** : **Dispatch**! [создан с помощью **FastAPI**]_"

Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix** [(ref)](https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072)

* * *

"_Я в полном восторге от**FastAPI**. Это так весело!_"

Brian Okken - **Ведущий подкаста [Python Bytes](https://pythonbytes.fm/episodes/show/123/time-to-right-the-py-wrongs?time_in_sec=855)** [(ref)](https://x.com/brianokken/status/1112220079972728832)

* * *

"_Честно говоря, то, что вы создали, выглядит очень солидно и отполировано. Во многих смыслах это то, чем я хотел видеть**Hug** — очень вдохновляет видеть, как кто-то это создал._"

Timothy Crosley - **Создатель [Hug](https://github.com/hugapi/hug)** [(ref)](https://news.ycombinator.com/item?id=19455465)

* * *

"_Если вы хотите изучить один**современный фреймворк** для создания REST API, посмотрите **FastAPI** [...] Он быстрый, простой в использовании и лёгкий в изучении [...]_"

"_Мы переключились на**FastAPI** для наших **API** [...] Думаю, вам тоже понравится [...]_"

Ines Montani - Matthew Honnibal - **Основатели [Explosion AI](https://explosion.ai) — создатели [spaCy](https://spacy.io)** [(ref)](https://x.com/_inesmontani/status/1144173225322143744) \- [(ref)](https://x.com/honnibal/status/1144031421859655680)

* * *

"_Если кто-то собирается делать продакшн-API на Python, я настоятельно рекомендую**FastAPI**. Он **прекрасно спроектирован** , **прост в использовании** и **отлично масштабируется** , стал **ключевым компонентом** нашей стратегии API-first и приводит в действие множество автоматизаций и сервисов, таких как наш Virtual TAC Engineer._"

Deon Pillsbury - **Cisco** [(ref)](https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-activity-6963242628536487936-trAp/)

* * *

## Мини-документальный фильм о FastAPI

В конце 2025 года вышел [мини-документальный фильм о FastAPI](https://www.youtube.com/watch?v=mpR8ngthqiE), вы можете посмотреть его онлайн:

[![FastAPI Mini Documentary](https://fastapi.tiangolo.com/img/fastapi-documentary.jpg)](https://www.youtube.com/watch?v=mpR8ngthqiE)

## **Typer** , FastAPI для CLI

[![](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)](https://typer.tiangolo.com)

Если вы создаёте приложение CLI для использования в терминале вместо веб-API, посмотрите [**Typer**](https://typer.tiangolo.com/).

**Typer** — младший брат FastAPI. И он задуман как **FastAPI для CLI**. ⌨️ 🚀

## Зависимости

FastAPI стоит на плечах гигантов:

  * [Starlette](https://www.starlette.dev/) для части, связанной с вебом.
  * [Pydantic](https://docs.pydantic.dev/) для части, связанной с данными.

## Установка

Создайте и активируйте [виртуальное окружение](https://fastapi.tiangolo.com/ru/virtual-environments/) ([local](./01_fastapi/06_обучение/04_виртуальные-окружения.md)), затем установите FastAPI:

```
 
    $ pip install "fastapi[standard]"
    
    ---> 100%
    

```

**Примечание** : Обязательно заключите `"fastapi[standard]"` в кавычки, чтобы это работало во всех терминалах.

## Пример

### Создание

Создайте файл `main.py` со следующим содержимым:

```
 
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: str | None = None):
        return {"item_id": item_id, "q": q}
    

```

Или используйте `async def`...

Если ваш код использует `async` / `await`, используйте `async def`:

```
 
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    async def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    async def read_item(item_id: int, q: str | None = None):
        return {"item_id": item_id, "q": q}
    

```

**Примечание** :

Если не уверены, посмотрите раздел _«Нет времени?»_ о [`async` и `await` в документации](https://fastapi.tiangolo.com/ru/async/#in-a-hurry) ([local](./01_fastapi/06_обучение/02_конкурентность-и-async-await.md#in-a-hurry)).

### Запуск

Запустите сервер командой:

```
 
    $ fastapi dev
    
     ╭────────── FastAPI CLI - Development mode ───────────╮
     │                                                     │
     │  Serving at: http://127.0.0.1:8000                  │
     │                                                     │
     │  API docs: http://127.0.0.1:8000/docs               │
     │                                                     │
     │  Running in development mode, for production use:   │
     │                                                     │
     │  fastapi run                                        │
     │                                                     │
     ╰─────────────────────────────────────────────────────╯
    
    INFO:     Will watch for changes in these directories: ['/home/user/code/awesomeapp']
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [2248755] using WatchFiles
    INFO:     Started server process [2248757]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    

```

О команде `fastapi dev`...

Команда `fastapi dev` читает ваш файл `main.py`, находит в нём приложение **FastAPI** и запускает сервер с помощью [Uvicorn](https://www.uvicorn.dev).

По умолчанию `fastapi dev` запускается с включённой авто-перезагрузкой для локальной разработки.

Подробнее в [документации по FastAPI CLI](https://fastapi.tiangolo.com/ru/fastapi-cli/) ([local](./01_fastapi/06_обучение/09_fastapi-cli.md)).

### Проверка

Откройте браузер на <http://127.0.0.1:8000/items/5?q=somequery>.

Вы увидите JSON-ответ:

```
 
    {"item_id": 5, "q": "somequery"}
    

```

Вы уже создали API, который:

  * Получает HTTP-запросы по _путям_ `/` и `/items/{item_id}`.
  * Оба _пути_ используют `GET` _операции_ (также известные как HTTP _методы_).
  * _Путь_ `/items/{item_id}` имеет _path-параметр_ `item_id`, который должен быть `int`.
  * _Путь_ `/items/{item_id}` имеет необязательный `str` _параметр запроса_ `q`.

### Интерактивная документация API

Перейдите на <http://127.0.0.1:8000/docs>.

Вы увидите автоматическую интерактивную документацию API (предоставлена [Swagger UI](https://github.com/swagger-api/swagger-ui)):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### Альтернативная документация API

Теперь откройте <http://127.0.0.1:8000/redoc>.

Вы увидите альтернативную автоматическую документацию (предоставлена [ReDoc](https://github.com/Rebilly/ReDoc)):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

## Пример обновления

Теперь измените файл `main.py`, чтобы принимать тело запроса из `PUT` HTTP-запроса.

Объявите тело запроса, используя стандартные типы Python, спасибо Pydantic.

```
 
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    app = FastAPI()
    
    
    class Item(BaseModel):
        name: str
        price: float
        is_offer: bool | None = None
    
    
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    
    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: str | None = None):
        return {"item_id": item_id, "q": q}
    
    
    @app.put("/items/{item_id}")
    def update_item(item_id: int, item: Item):
        return {"item_name": item.name, "item_id": item_id}
    

```

Сервер `fastapi dev` должен перезагрузиться автоматически.

### Обновление интерактивной документации API

Перейдите на <http://127.0.0.1:8000/docs>.

  * Интерактивная документация API будет автоматически обновлена, включая новое тело запроса:

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

  * Нажмите кнопку «Try it out», это позволит вам заполнить параметры и напрямую взаимодействовать с API:

![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)

  * Затем нажмите кнопку «Execute», интерфейс свяжется с вашим API, отправит параметры, получит результаты и отобразит их на экране:

![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)

### Обновление альтернативной документации API

Теперь откройте <http://127.0.0.1:8000/redoc>.

  * Альтернативная документация также отразит новый параметр запроса и тело запроса:

![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

### Подведём итоги

Итак, вы объявляете **один раз** типы параметров, тело запроса и т.д. как параметры функции.

Вы делаете это с помощью стандартных современных типов Python.

Вам не нужно изучать новый синтаксис, методы или классы конкретной библиотеки и т.п.

Только стандартный **Python**.

Например, для `int`:

```
 
    item_id: int
    

```

или для более сложной модели `Item`:

```
 
    item: Item
    

```

...и с этим единственным объявлением вы получаете:

  * Поддержку редактора кода, включая:
    * Автозавершение.
    * Проверку типов.
  * Валидацию данных:
    * Автоматические и понятные ошибки, когда данные некорректны.
    * Валидацию даже для глубоко вложенных объектов JSON.
  * Преобразование входных данных: из сети в данные и типы Python. Чтение из:
    * JSON.
    * Параметров пути.
    * Параметров запроса.
    * Cookies.
    * HTTP-заголовков.
    * Форм.
    * Файлов.
  * Преобразование выходных данных: из данных и типов Python в данные сети (например, JSON):
    * Преобразование типов Python (`str`, `int`, `float`, `bool`, `list` и т.д.).
    * Объекты `datetime`.
    * Объекты `UUID`.
    * Модели баз данных.
    * ...и многое другое.
  * Автоматическую интерактивную документацию API, включая 2 альтернативных интерфейса:
    * Swagger UI.
    * ReDoc.

* * *

Возвращаясь к предыдущему примеру кода, **FastAPI** будет:

  * Валидировать наличие `item_id` в пути для `GET` и `PUT` HTTP-запросов.
  * Валидировать, что `item_id` имеет тип `int` для `GET` и `PUT` HTTP-запросов.
    * Если это не так, клиент увидит полезную понятную ошибку.
  * Проверять, есть ли необязательный параметр запроса с именем `q` (например, `http://127.0.0.1:8000/items/foo?q=somequery`) для `GET` HTTP-запросов.
    * Поскольку параметр `q` объявлен с `= None`, он необязателен.
    * Без `None` он был бы обязательным (как тело запроса в случае с `PUT`).
  * Для `PUT` HTTP-запросов к `/items/{item_id}` читать тело запроса как JSON:
    * Проверять, что есть обязательный атрибут `name`, который должен быть `str`.
    * Проверять, что есть обязательный атрибут `price`, который должен быть `float`.
    * Проверять, что есть необязательный атрибут `is_offer`, который должен быть `bool`, если он присутствует.
    * Всё это также будет работать для глубоко вложенных объектов JSON.
  * Автоматически преобразовывать из и в JSON.
  * Документировать всё с помощью OpenAPI, что может быть использовано:
    * Системами интерактивной документации.
    * Системами автоматической генерации клиентского кода для многих языков.
  * Предоставлять 2 веб-интерфейса интерактивной документации напрямую.

* * *

Мы только поверхностно ознакомились, но вы уже понимаете, как всё это работает.

Попробуйте изменить строку:

```
 
        return {"item_name": item.name, "item_id": item_id}
    

```

...из:

```
 
            ... "item_name": item.name ...
    

```

...на:

```
 
            ... "item_price": item.price ...
    

```

...и посмотрите, как ваш редактор кода будет автоматически дополнять атрибуты и знать их типы:

![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)

Более полный пример с дополнительными возможностями см. в [Учебник - Руководство пользователя](https://fastapi.tiangolo.com/ru/tutorial/) ([local](./01_fastapi/06_обучение/05_учебник-руководство-пользователя.md)).

**Осторожно, спойлер** : учебник - руководство пользователя включает:

  * Объявление **параметров** из других источников: **HTTP-заголовки** , **cookies** , **поля формы** и **файлы**.
  * Как задать **ограничения валидации** вроде `maximum_length` или `regex`.
  * Очень мощную и простую в использовании систему **внедрения зависимостей**.
  * Безопасность и аутентификацию, включая поддержку **OAuth2** с **JWT токенами** и **HTTP Basic** аутентификацию.
  * Более продвинутые (но столь же простые) приёмы объявления **глубоко вложенных JSON-моделей** (спасибо Pydantic).
  * Интеграцию **GraphQL** с [Strawberry](https://strawberry.rocks) и другими библиотеками.
  * Множество дополнительных функций (благодаря Starlette), таких как:
    * **WebSockets**
    * чрезвычайно простые тесты на основе HTTPX и `pytest`
    * **CORS**
    * **сессии с использованием cookie**
    * ...и многое другое.

### Разверните приложение (опционально)

При желании вы можете развернуть своё приложение FastAPI в [FastAPI Cloud](https://fastapicloud.com), присоединяйтесь к списку ожидания, если ещё не сделали этого. 🚀

Если у вас уже есть аккаунт **FastAPI Cloud** (мы пригласили вас из списка ожидания 😉), вы можете развернуть ваше приложение одной командой.

```
 
    $ fastapi deploy
    
    Deploying to FastAPI Cloud...
    
    ✅ Deployment successful!
    
    🐔 Ready the chicken! Your app is ready at https://myapp.fastapicloud.dev
    

```

Вот и всё! Теперь вы можете открыть ваше приложение по этой ссылке. ✨

#### О FastAPI Cloud

**[FastAPI Cloud](https://fastapicloud.com)** создан тем же автором и командой, что и **FastAPI**.

Он упрощает процесс **создания образа** , **развертывания** и **доступа** к API при минимальных усилиях.

Он переносит тот же **опыт разработчика** , что и при создании приложений на FastAPI, на их **развертывание** в облаке. 🎉

FastAPI Cloud — основной спонсор и источник финансирования для проектов с открытым исходным кодом из экосистемы _FastAPI and friends_. ✨

#### Развертывание у других облачных провайдеров

FastAPI — это open source и стандартизированный фреймворк. Вы можете развернуть приложения FastAPI у любого облачного провайдера на ваш выбор.

Следуйте руководствам вашего облачного провайдера по развертыванию приложений FastAPI. 🤓

## Производительность

Независимые бенчмарки TechEmpower показывают приложения **FastAPI** , работающие под управлением Uvicorn, как [один из самых быстрых доступных фреймворков Python](https://www.techempower.com/benchmarks/#section=test&runid=7464e520-0dc2-473d-bd34-dbdfd7e85911&hw=ph&test=query&l=zijzen-7), уступающий только самим Starlette и Uvicorn (используются внутри FastAPI). (*)

Чтобы узнать больше, см. раздел [Бенчмарки](https://fastapi.tiangolo.com/ru/benchmarks/) ([local](./01_fastapi/13_о-проекте/03_бенчмарки-тесты-производительности.md)).

## Зависимости

FastAPI зависит от Pydantic и Starlette.

### Зависимости `standard`

Когда вы устанавливаете FastAPI с помощью `pip install "fastapi[standard]"`, он идёт с группой опциональных зависимостей `standard`:

Используется Pydantic:

  * [`email-validator`](https://github.com/JoshData/python-email-validator) — для проверки адресов электронной почты.

Используется Starlette:

  * [`httpx`](https://www.python-httpx.org) — обязателен, если вы хотите использовать `TestClient`.
  * [`jinja2`](https://jinja.palletsprojects.com) — обязателен, если вы хотите использовать конфигурацию шаблонов по умолчанию.
  * [`python-multipart`](https://github.com/Kludex/python-multipart) \- обязателен, если вы хотите поддерживать «парсинг» форм через `request.form()`.

Используется FastAPI:

  * [`uvicorn`](https://www.uvicorn.dev) — сервер, который загружает и «отдаёт» ваше приложение. Включает `uvicorn[standard]`, содержащий некоторые зависимости (например, `uvloop`), нужные для высокой производительности.
  * `fastapi-cli[standard]` — чтобы предоставить команду `fastapi`.
    * Включает `fastapi-cloud-cli`, который позволяет развернуть ваше приложение FastAPI в [FastAPI Cloud](https://fastapicloud.com).

### Без зависимостей `standard`

Если вы не хотите включать опциональные зависимости `standard`, можно установить `pip install fastapi` вместо `pip install "fastapi[standard]"`.

### Без `fastapi-cloud-cli`

Если вы хотите установить FastAPI со стандартными зависимостями, но без `fastapi-cloud-cli`, установите `pip install "fastapi[standard-no-fastapi-cloud-cli]"`.

### Дополнительные опциональные зависимости

Есть дополнительные зависимости, которые вы можете установить.

Дополнительные опциональные зависимости Pydantic:

  * [`pydantic-settings`](https://docs.pydantic.dev/latest/usage/pydantic_settings/) — для управления настройками.
  * [`pydantic-extra-types`](https://docs.pydantic.dev/latest/usage/types/extra_types/extra_types/) — дополнительные типы для использования с Pydantic.

Дополнительные опциональные зависимости FastAPI:

  * [`orjson`](https://github.com/ijl/orjson) — обязателен, если вы хотите использовать `ORJSONResponse`.
  * [`ujson`](https://github.com/esnme/ultrajson) — обязателен, если вы хотите использовать `UJSONResponse`.

## Лицензия

Этот проект распространяется на условиях лицензии MIT.
  *[CLI]: Command Line Interface - Интерфейс командной строки
