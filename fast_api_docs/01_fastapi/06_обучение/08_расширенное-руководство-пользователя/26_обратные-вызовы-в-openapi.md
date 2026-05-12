---
title: Обратные вызовы в OpenAPI
source: https://fastapi.tiangolo.com/ru/advanced/openapi-callbacks/
---

# Обратные вызовы в OpenAPI

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/advanced/openapi-callbacks/)

Вы можете создать API с _операцией пути_ (обработчиком пути), которая будет инициировать HTTP-запрос к _внешнему API_ , созданному кем-то другим (скорее всего тем же разработчиком, который будет использовать ваш API).

Процесс, происходящий, когда ваше приложение API обращается к _внешнему API_ , называется «callback» (обратный вызов). Программное обеспечение, написанное внешним разработчиком, отправляет HTTP-запрос вашему API, а затем ваш API выполняет обратный вызов, отправляя HTTP-запрос во _внешний API_ (который, вероятно, тоже создал тот же разработчик).

В этом случае вам может понадобиться задокументировать, как должно выглядеть это внешнее API: какую _операцию пути_ оно должно иметь, какое тело запроса ожидать, какой ответ возвращать и т.д.

## Приложение с обратными вызовами

Давайте рассмотрим это на примере.

Представьте, что вы разрабатываете приложение, позволяющее создавать счета.

Эти счета будут иметь `id`, `title` (необязательный), `customer` и `total`.

Пользователь вашего API (внешний разработчик) создаст счет в вашем API с помощью POST-запроса.

Затем ваш API (предположим) сделает следующее:

  * Отправит счет клиенту внешнего разработчика.
  * Получит оплату.
  * Отправит уведомление обратно пользователю API (внешнему разработчику).
    * Это будет сделано отправкой POST-запроса (из _вашего API_) в _внешний API_ , предоставленный этим внешним разработчиком (это и есть «callback»).

## Обычное приложение **FastAPI**

Сначала посмотрим, как будет выглядеть обычное приложение API до добавления обратного вызова.

В нём будет _операция пути_ , которая получит тело запроса `Invoice`, и query-параметр `callback_url`, содержащий URL для обратного вызова.

Эта часть вполне обычна, большая часть кода вам уже знакома:

Python 3.10+

```
 
    from fastapi import APIRouter, FastAPI
    from pydantic import BaseModel, HttpUrl
    
    app = FastAPI()
    
    
    class Invoice(BaseModel):
        id: str
        title: str | None = None
        customer: str
        total: float
    
    
    class InvoiceEvent(BaseModel):
        description: str
        paid: bool
    
    
    class InvoiceEventReceived(BaseModel):
        ok: bool
    
    
    invoices_callback_router = APIRouter()
    
    
    @invoices_callback_router.post(
        "{$callback_url}/invoices/{$request.body.id}", response_model=InvoiceEventReceived
    )
    def invoice_notification(body: InvoiceEvent):
        pass
    
    
    @app.post("/invoices/", callbacks=invoices_callback_router.routes)
    def create_invoice(invoice: Invoice, callback_url: HttpUrl | None = None):
        """
        Create an invoice.
    
        This will (let's imagine) let the API user (some external developer) create an
        invoice.
    
        And this path operation will:
    
        * Send the invoice to the client.
        * Collect the money from the client.
        * Send a notification back to the API user (the external developer), as a callback.
            * At this point is that the API will somehow send a POST request to the
                external API with the notification of the invoice event
                (e.g. "payment successful").
        """
        # Send the invoice, collect the money, send the notification (the callback)
        return {"msg": "Invoice received"}
    

```

Совет

Query-параметр `callback_url` использует тип Pydantic [Url](https://docs.pydantic.dev/latest/api/networks/).

Единственное новое — это `callbacks=invoices_callback_router.routes` в качестве аргумента _декоратора операции пути_. Далее разберёмся, что это такое.

## Документирование обратного вызова

Реальный код обратного вызова будет сильно зависеть от вашего приложения API.

И, вероятно, он будет заметно отличаться от одного приложения к другому.

Это могут быть буквально одна-две строки кода, например:

```
 
    callback_url = "https://example.com/api/v1/invoices/events/"
    httpx.post(callback_url, json={"description": "Invoice paid", "paid": True})
    

```

Но, возможно, самая важная часть обратного вызова — это убедиться, что пользователь вашего API (внешний разработчик) правильно реализует _внешний API_ в соответствии с данными, которые _ваш API_ будет отправлять в теле запроса обратного вызова и т.п.

Поэтому далее мы добавим код, документирующий, как должен выглядеть этот _внешний API_ , чтобы получать обратный вызов от _вашего API_.

Эта документация отобразится в Swagger UI по адресу `/docs` в вашем API и позволит внешним разработчикам понять, как построить _внешний API_.

В этом примере сам обратный вызов не реализуется (это может быть всего одна строка кода), реализуется только часть с документацией.

Совет

Сам обратный вызов — это всего лишь HTTP-запрос.

Реализуя обратный вызов, вы можете использовать, например, [HTTPX](https://www.python-httpx.org) или [Requests](https://requests.readthedocs.io/).

## Напишите код документации обратного вызова

Этот код не будет выполняться в вашем приложении, он нужен только для _документирования_ того, как должен выглядеть _внешний API_.

Но вы уже знаете, как легко получить автоматическую документацию для API с **FastAPI**.

Мы используем те же знания, чтобы задокументировать, как должен выглядеть _внешний API_... создав _операции пути_ , которые внешний API должен реализовать (те, которые ваш API будет вызывать).

Совет

Когда вы пишете код для документирования обратного вызова, полезно представить, что вы — тот самый _внешний разработчик_. И что вы сейчас реализуете _внешний API_ , а не _свой API_.

Временное принятие этой точки зрения (внешнего разработчика) поможет интуитивно понять, куда поместить параметры, какую Pydantic-модель использовать для тела запроса, для ответа и т.д. во _внешнем API_.

### Создайте `APIRouter` для обратного вызова

Сначала создайте новый `APIRouter`, который будет содержать один или несколько обратных вызовов.

Python 3.10+

```
 
    from fastapi import APIRouter, FastAPI
    from pydantic import BaseModel, HttpUrl
    
    app = FastAPI()
    
    
    class Invoice(BaseModel):
        id: str
        title: str | None = None
        customer: str
        total: float
    
    
    class InvoiceEvent(BaseModel):
        description: str
        paid: bool
    
    
    class InvoiceEventReceived(BaseModel):
        ok: bool
    
    
    invoices_callback_router = APIRouter()
    
    
    @invoices_callback_router.post(
        "{$callback_url}/invoices/{$request.body.id}", response_model=InvoiceEventReceived
    )
    def invoice_notification(body: InvoiceEvent):
        pass
    
    
    @app.post("/invoices/", callbacks=invoices_callback_router.routes)
    def create_invoice(invoice: Invoice, callback_url: HttpUrl | None = None):
        """
        Create an invoice.
    
        This will (let's imagine) let the API user (some external developer) create an
        invoice.
    
        And this path operation will:
    
        * Send the invoice to the client.
        * Collect the money from the client.
        * Send a notification back to the API user (the external developer), as a callback.
            * At this point is that the API will somehow send a POST request to the
                external API with the notification of the invoice event
                (e.g. "payment successful").
        """
        # Send the invoice, collect the money, send the notification (the callback)
        return {"msg": "Invoice received"}
    

```

### Создайте _операцию пути_ для обратного вызова

Чтобы создать _операцию пути_ для обратного вызова, используйте тот же `APIRouter`, который вы создали выше.

Она должна выглядеть как обычная _операция пути_ FastAPI:

  * Вероятно, в ней должно быть объявление тела запроса, например `body: InvoiceEvent`.
  * А также может быть объявление модели ответа, например `response_model=InvoiceEventReceived`.

Python 3.10+

```
 
    from fastapi import APIRouter, FastAPI
    from pydantic import BaseModel, HttpUrl
    
    app = FastAPI()
    
    
    class Invoice(BaseModel):
        id: str
        title: str | None = None
        customer: str
        total: float
    
    
    class InvoiceEvent(BaseModel):
        description: str
        paid: bool
    
    
    class InvoiceEventReceived(BaseModel):
        ok: bool
    
    
    invoices_callback_router = APIRouter()
    
    
    @invoices_callback_router.post(
        "{$callback_url}/invoices/{$request.body.id}", response_model=InvoiceEventReceived
    )
    def invoice_notification(body: InvoiceEvent):
        pass
    
    
    @app.post("/invoices/", callbacks=invoices_callback_router.routes)
    def create_invoice(invoice: Invoice, callback_url: HttpUrl | None = None):
        """
        Create an invoice.
    
        This will (let's imagine) let the API user (some external developer) create an
        invoice.
    
        And this path operation will:
    
        * Send the invoice to the client.
        * Collect the money from the client.
        * Send a notification back to the API user (the external developer), as a callback.
            * At this point is that the API will somehow send a POST request to the
                external API with the notification of the invoice event
                (e.g. "payment successful").
        """
        # Send the invoice, collect the money, send the notification (the callback)
        return {"msg": "Invoice received"}
    

```

Есть 2 основных отличия от обычной _операции пути_ :

  * Ей не нужен реальный код, потому что ваше приложение никогда не будет вызывать эту функцию. Она используется только для документирования _внешнего API_. Поэтому в функции может быть просто `pass`.
  * _Путь_ может содержать [выражение OpenAPI 3](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.1.0.md#key-expression) (подробнее ниже), где можно использовать переменные с параметрами и части исходного HTTP-запроса, отправленного _вашему API_.

### Выражение пути для обратного вызова

_Путь_ обратного вызова может содержать [выражение OpenAPI 3](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.1.0.md#key-expression), которое может включать части исходного запроса, отправленного _вашему API_.

В нашем случае это `str`:

```
 
    "{$callback_url}/invoices/{$request.body.id}"
    

```

Итак, если пользователь вашего API (внешний разработчик) отправляет HTTP-запрос вашему API по адресу:

```
 
    https://yourapi.com/invoices/?callback_url=https://www.external.org/events
    

```

с телом JSON:

```
 
    {
        "id": "2expen51ve",
        "customer": "Mr. Richie Rich",
        "total": "9999"
    }
    

```

то _ваш API_ обработает счёт и, в какой-то момент позже, отправит запрос обратного вызова на `callback_url` (_внешний API_):

```
 
    https://www.external.org/events/invoices/2expen51ve
    

```

с телом JSON примерно такого вида:

```
 
    {
        "description": "Payment celebration",
        "paid": true
    }
    

```

и будет ожидать от _внешнего API_ ответ с телом JSON вида:

```
 
    {
        "ok": true
    }
    

```

Совет

Обратите внимание, что используемый URL обратного вызова содержит URL, полученный как query-параметр в `callback_url` (`https://www.external.org/events`), а также `id` счёта из тела JSON (`2expen51ve`).

### Подключите маршрутизатор обратного вызова

К этому моменту у вас есть необходимые _операции пути_ обратного вызова (те, которые _внешний разработчик_ должен реализовать во _внешнем API_) в созданном выше маршрутизаторе обратных вызовов.

Теперь используйте параметр `callbacks` в _декораторе операции пути вашего API_ , чтобы передать атрибут `.routes` (это, по сути, просто `list` маршрутов/_операций пути_) из этого маршрутизатора обратных вызовов:

Python 3.10+

```
 
    from fastapi import APIRouter, FastAPI
    from pydantic import BaseModel, HttpUrl
    
    app = FastAPI()
    
    
    class Invoice(BaseModel):
        id: str
        title: str | None = None
        customer: str
        total: float
    
    
    class InvoiceEvent(BaseModel):
        description: str
        paid: bool
    
    
    class InvoiceEventReceived(BaseModel):
        ok: bool
    
    
    invoices_callback_router = APIRouter()
    
    
    @invoices_callback_router.post(
        "{$callback_url}/invoices/{$request.body.id}", response_model=InvoiceEventReceived
    )
    def invoice_notification(body: InvoiceEvent):
        pass
    
    
    @app.post("/invoices/", callbacks=invoices_callback_router.routes)
    def create_invoice(invoice: Invoice, callback_url: HttpUrl | None = None):
        """
        Create an invoice.
    
        This will (let's imagine) let the API user (some external developer) create an
        invoice.
    
        And this path operation will:
    
        * Send the invoice to the client.
        * Collect the money from the client.
        * Send a notification back to the API user (the external developer), as a callback.
            * At this point is that the API will somehow send a POST request to the
                external API with the notification of the invoice event
                (e.g. "payment successful").
        """
        # Send the invoice, collect the money, send the notification (the callback)
        return {"msg": "Invoice received"}
    

```

Совет

Обратите внимание, что вы передаёте не сам маршрутизатор (`invoices_callback_router`) в `callback=`, а его атрибут `.routes`, то есть `invoices_callback_router.routes`.

### Проверьте документацию

Теперь вы можете запустить приложение и перейти по адресу <http://127.0.0.1:8000/docs>.

Вы увидите документацию, включающую раздел «Callbacks» для вашей _операции пути_ , который показывает, как должен выглядеть _внешний API_ :

![](https://fastapi.tiangolo.com/img/tutorial/openapi-callbacks/image01.png)
