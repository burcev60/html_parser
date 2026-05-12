---
title: JSON с байтами в Base64
source: https://fastapi.tiangolo.com/ru/advanced/json-base64-bytes/
---

# JSON с байтами в Base64

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/advanced/json-base64-bytes/)

Если вашему приложению нужно принимать и отправлять JSON-данные, но при этом необходимо включать в них бинарные данные, вы можете кодировать их в base64.

## Base64 и файлы

Сначала рассмотрите возможность использовать [Файлы в запросе](https://fastapi.tiangolo.com/ru/tutorial/request-files/) ([local](./../06_учебник-руководство-пользователя/22_загрузка-файлов.md)) для загрузки бинарных данных и [Пользовательский HTTP-ответ — FileResponse](https://fastapi.tiangolo.com/ru/advanced/custom-response/#fileresponse--fileresponse-) ([local](./05_кастомные-ответы-html-поток-файл-и-другие.md#fileresponse--fileresponse-)) для отправки бинарных данных вместо кодирования их в JSON.

JSON может содержать только строки в кодировке UTF-8, поэтому он не может содержать «сырые» байты.

Base64 может кодировать бинарные данные в строки, но для этого используется больше символов, чем в исходных бинарных данных, поэтому обычно это менее эффективно, чем обычные файлы.

Используйте base64 только если вам действительно нужно включать бинарные данные в JSON и вы не можете использовать файлы для этого.

## Pydantic `bytes`

Вы можете объявить Pydantic-модель с полями `bytes`, а затем использовать `val_json_bytes` в конфиге модели, чтобы указать использовать base64 для валидации входящих JSON-данных; как часть этой валидации строка base64 будет декодирована в байты.

Python 3.10+

```
 
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    
    class DataInput(BaseModel):
        description: str
        data: bytes
    
        model_config = {"val_json_bytes": "base64"}
    
    # Code here omitted 👈
    
    app = FastAPI()
    
    
    @app.post("/data")
    def post_data(body: DataInput):
        content = body.data.decode("utf-8")
        return {"description": body.description, "content": content}
    
    # Code below omitted 👇
    

```

👀 Full file preview

Python 3.10+

```
 
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    
    class DataInput(BaseModel):
        description: str
        data: bytes
    
        model_config = {"val_json_bytes": "base64"}
    
    
    class DataOutput(BaseModel):
        description: str
        data: bytes
    
        model_config = {"ser_json_bytes": "base64"}
    
    
    class DataInputOutput(BaseModel):
        description: str
        data: bytes
    
        model_config = {
            "val_json_bytes": "base64",
            "ser_json_bytes": "base64",
        }
    
    
    app = FastAPI()
    
    
    @app.post("/data")
    def post_data(body: DataInput):
        content = body.data.decode("utf-8")
        return {"description": body.description, "content": content}
    
    
    @app.get("/data")
    def get_data() -> DataOutput:
        data = "hello".encode("utf-8")
        return DataOutput(description="A plumbus", data=data)
    
    
    @app.post("/data-in-out")
    def post_data_in_out(body: DataInputOutput) -> DataInputOutput:
        return body
    

```

Если вы откроете `/docs`, вы увидите, что поле `data` ожидает байты, закодированные в base64:

![](https://fastapi.tiangolo.com/img/tutorial/json-base64-bytes/image01.png)

Вы можете отправить такой HTTP-запрос:

```
 
    {
        "description": "Some data",
        "data": "aGVsbG8="
    }
    

```

Совет

`aGVsbG8=` — это base64-кодирование строки `hello`.

Затем Pydantic декодирует строку base64 и передаст вам исходные байты в поле `data` модели.

Вы получите такой HTTP-ответ:

```
 
    {
      "description": "Some data",
      "content": "hello"
    }
    

```

## Pydantic `bytes` для выходных данных

Вы также можете использовать поля `bytes` с `ser_json_bytes` в конфиге модели для выходных данных, и Pydantic будет сериализовать байты в base64 при формировании JSON-ответа.

Python 3.10+

```
 
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    # Code here omitted 👈
    
    class DataOutput(BaseModel):
        description: str
        data: bytes
    
        model_config = {"ser_json_bytes": "base64"}
    
    # Code here omitted 👈
    
    app = FastAPI()
    
    # Code here omitted 👈
    
    @app.get("/data")
    def get_data() -> DataOutput:
        data = "hello".encode("utf-8")
        return DataOutput(description="A plumbus", data=data)
    
    # Code below omitted 👇
    

```

👀 Full file preview

Python 3.10+

```
 
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    
    class DataInput(BaseModel):
        description: str
        data: bytes
    
        model_config = {"val_json_bytes": "base64"}
    
    
    class DataOutput(BaseModel):
        description: str
        data: bytes
    
        model_config = {"ser_json_bytes": "base64"}
    
    
    class DataInputOutput(BaseModel):
        description: str
        data: bytes
    
        model_config = {
            "val_json_bytes": "base64",
            "ser_json_bytes": "base64",
        }
    
    
    app = FastAPI()
    
    
    @app.post("/data")
    def post_data(body: DataInput):
        content = body.data.decode("utf-8")
        return {"description": body.description, "content": content}
    
    
    @app.get("/data")
    def get_data() -> DataOutput:
        data = "hello".encode("utf-8")
        return DataOutput(description="A plumbus", data=data)
    
    
    @app.post("/data-in-out")
    def post_data_in_out(body: DataInputOutput) -> DataInputOutput:
        return body
    

```

## Pydantic `bytes` для входных и выходных данных

И, конечно, вы можете использовать одну и ту же модель, настроенную на использование base64, чтобы обрабатывать и входящие данные (валидация) с `val_json_bytes`, и исходящие данные (сериализация) с `ser_json_bytes` при приеме и отправке JSON-данных.

Python 3.10+

```
 
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    # Code here omitted 👈
    
    class DataInputOutput(BaseModel):
        description: str
        data: bytes
    
        model_config = {
            "val_json_bytes": "base64",
            "ser_json_bytes": "base64",
        }
    
    # Code here omitted 👈
    
    app = FastAPI()
    
    # Code here omitted 👈
    
    @app.post("/data-in-out")
    def post_data_in_out(body: DataInputOutput) -> DataInputOutput:
        return body
    

```

👀 Full file preview

Python 3.10+

```
 
    from fastapi import FastAPI
    from pydantic import BaseModel
    
    
    class DataInput(BaseModel):
        description: str
        data: bytes
    
        model_config = {"val_json_bytes": "base64"}
    
    
    class DataOutput(BaseModel):
        description: str
        data: bytes
    
        model_config = {"ser_json_bytes": "base64"}
    
    
    class DataInputOutput(BaseModel):
        description: str
        data: bytes
    
        model_config = {
            "val_json_bytes": "base64",
            "ser_json_bytes": "base64",
        }
    
    
    app = FastAPI()
    
    
    @app.post("/data")
    def post_data(body: DataInput):
        content = body.data.decode("utf-8")
        return {"description": body.description, "content": content}
    
    
    @app.get("/data")
    def get_data() -> DataOutput:
        data = "hello".encode("utf-8")
        return DataOutput(description="A plumbus", data=data)
    
    
    @app.post("/data-in-out")
    def post_data_in_out(body: DataInputOutput) -> DataInputOutput:
        return body
    

```
