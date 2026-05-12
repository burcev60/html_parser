---
title: Path-параметры
source: https://fastapi.tiangolo.com/ru/tutorial/path-params/
---

# Path-параметры

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/tutorial/path-params/)

Вы можете определить "параметры" или "переменные" пути, используя синтаксис форматированных строк Python:

Python 3.10+

```
 
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/items/{item_id}")
    async def read_item(item_id):
        return {"item_id": item_id}
    

```

Значение параметра пути `item_id` будет передано в функцию в качестве аргумента `item_id`.

Если запустите этот пример и перейдёте по адресу: <http://127.0.0.1:8000/items/foo>, то увидите ответ:

```
 
    {"item_id":"foo"}
    

```

## Параметры пути с типами

Вы можете объявить тип параметра пути в функции, используя стандартные аннотации типов Python:

Python 3.10+

```
 
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/items/{item_id}")
    async def read_item(item_id: int):
        return {"item_id": item_id}
    

```

Здесь, `item_id` объявлен типом `int`.

Заметка

Это обеспечит поддержку редактора кода внутри функции (проверка ошибок, автозавершение и т.п.).

## Преобразование данных

Если запустите этот пример и перейдёте по адресу: <http://127.0.0.1:8000/items/3>, то увидите ответ:

```
 
    {"item_id":3}
    

```

Заметка

Обратите внимание на значение `3`, которое получила (и вернула) функция. Это целочисленный Python `int`, а не строка `"3"`.

Используя такое объявление типов, **FastAPI** выполняет автоматический HTTP-запрос "парсинг".

## Валидация данных

Если откроете браузер по адресу <http://127.0.0.1:8000/items/foo>, то увидите интересную HTTP-ошибку:

```
 
    {
      "detail": [
        {
          "type": "int_parsing",
          "loc": [
            "path",
            "item_id"
          ],
          "msg": "Input should be a valid integer, unable to parse string as an integer",
          "input": "foo"
        }
      ]
    }
    

```

из-за того, что параметр пути `item_id` имеет значение `"foo"`, которое не является типом `int`.

Та же ошибка возникнет, если вместо `int` передать `float`, например: <http://127.0.0.1:8000/items/4.2>

Заметка

**FastAPI** обеспечивает валидацию данных, используя всё те же определения типов.

Обратите внимание, что в тексте ошибки явно указано место, не прошедшее проверку.

Это очень полезно при разработке и отладке кода, который взаимодействует с API.

## Документация

И теперь, когда откроете браузер по адресу: <http://127.0.0.1:8000/docs>, то увидите вот такую автоматически сгенерированную документацию API:

![](https://fastapi.tiangolo.com/img/tutorial/path-params/image01.png)

Заметка

Ещё раз, просто используя определения типов, **FastAPI** обеспечивает автоматическую интерактивную документацию (с интеграцией Swagger UI).

Обратите внимание, что параметр пути объявлен целочисленным.

## Преимущества стандартизации, альтернативная документация

Поскольку сгенерированная схема соответствует стандарту [OpenAPI](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.1.0.md), её можно использовать со множеством совместимых инструментов.

Именно поэтому, **FastAPI** сам предоставляет альтернативную документацию API (используя ReDoc), которую можно получить по адресу: <http://127.0.0.1:8000/redoc>.

![](https://fastapi.tiangolo.com/img/tutorial/path-params/image02.png)

По той же причине, есть множество совместимых инструментов, включая инструменты генерации кода для многих языков.

## Pydantic

Вся проверка данных выполняется под капотом с помощью [Pydantic](https://docs.pydantic.dev/), поэтому вы получаете все его преимущества. И вы можете быть уверены, что находитесь в надёжных руках.

Вы можете использовать в аннотациях как простые типы данных, вроде `str`, `float`, `bool`, так и более сложные типы.

Некоторые из них рассматриваются в следующих главах данного руководства.

## Порядок имеет значение

При создании _операций пути_ можно столкнуться с ситуацией, когда путь является фиксированным.

Например, `/users/me`. Предположим, что это путь для получения данных о текущем пользователе.

У вас также может быть путь `/users/{user_id}`, чтобы получить данные о конкретном пользователе по его ID.

Поскольку _операции пути_ выполняются в порядке их объявления, необходимо, чтобы путь для `/users/me` был объявлен раньше, чем путь для `/users/{user_id}`:

Python 3.10+

```
 
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/users/me")
    async def read_user_me():
        return {"user_id": "the current user"}
    
    
    @app.get("/users/{user_id}")
    async def read_user(user_id: str):
        return {"user_id": user_id}
    

```

Иначе путь для `/users/{user_id}` также будет соответствовать `/users/me`, "подразумевая", что он получает параметр `user_id` со значением `"me"`.

Аналогично, вы не можете переопределить операцию с путем:

Python 3.10+

```
 
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/users")
    async def read_users():
        return ["Rick", "Morty"]
    
    
    @app.get("/users")
    async def read_users2():
        return ["Bean", "Elfo"]
    

```

Первый будет выполняться всегда, так как путь совпадает первым.

## Предопределенные значения

Что если нам нужно заранее определить допустимые _параметры пути_ , которые _операция пути_ может принимать? В таком случае можно использовать стандартное перечисление `Enum` Python.

### Создание класса `Enum`

Импортируйте `Enum` и создайте подкласс, который наследуется от `str` и `Enum`.

Мы наследуемся от `str`, чтобы документация API могла понять, что значения должны быть типа `string` и отображалась правильно.

Затем создайте атрибуты класса с фиксированными допустимыми значениями:

Python 3.10+

```
 
    from enum import Enum
    
    from fastapi import FastAPI
    
    
    class ModelName(str, Enum):
        alexnet = "alexnet"
        resnet = "resnet"
        lenet = "lenet"
    
    
    app = FastAPI()
    
    
    @app.get("/models/{model_name}")
    async def get_model(model_name: ModelName):
        if model_name is ModelName.alexnet:
            return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
        if model_name.value == "lenet":
            return {"model_name": model_name, "message": "LeCNN all the images"}
    
        return {"model_name": model_name, "message": "Have some residuals"}
    

```

Подсказка

Если интересно, то "AlexNet", "ResNet" и "LeNet" - это названия моделей Машинного обучения.

### Определение _параметра пути_

Определите _параметр пути_ , используя в аннотации типа класс перечисления (`ModelName`), созданный ранее:

Python 3.10+

```
 
    from enum import Enum
    
    from fastapi import FastAPI
    
    
    class ModelName(str, Enum):
        alexnet = "alexnet"
        resnet = "resnet"
        lenet = "lenet"
    
    
    app = FastAPI()
    
    
    @app.get("/models/{model_name}")
    async def get_model(model_name: ModelName):
        if model_name is ModelName.alexnet:
            return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
        if model_name.value == "lenet":
            return {"model_name": model_name, "message": "LeCNN all the images"}
    
        return {"model_name": model_name, "message": "Have some residuals"}
    

```

### Проверьте документацию

Поскольку доступные значения _параметра пути_ определены заранее, интерактивная документация может наглядно их отображать:

![](https://fastapi.tiangolo.com/img/tutorial/path-params/image03.png)

### Работа с _перечислениями_ в Python

Значение _параметра пути_ будет _элементом перечисления_.

#### Сравнение _элементов перечисления_

Вы можете сравнить это значение с _элементом перечисления_ класса `ModelName`:

Python 3.10+

```
 
    from enum import Enum
    
    from fastapi import FastAPI
    
    
    class ModelName(str, Enum):
        alexnet = "alexnet"
        resnet = "resnet"
        lenet = "lenet"
    
    
    app = FastAPI()
    
    
    @app.get("/models/{model_name}")
    async def get_model(model_name: ModelName):
        if model_name is ModelName.alexnet:
            return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
        if model_name.value == "lenet":
            return {"model_name": model_name, "message": "LeCNN all the images"}
    
        return {"model_name": model_name, "message": "Have some residuals"}
    

```

#### Получение _значения перечисления_

Можно получить фактическое значение (в данном случае - `str`) с помощью `model_name.value` или в общем случае `your_enum_member.value`:

Python 3.10+

```
 
    from enum import Enum
    
    from fastapi import FastAPI
    
    
    class ModelName(str, Enum):
        alexnet = "alexnet"
        resnet = "resnet"
        lenet = "lenet"
    
    
    app = FastAPI()
    
    
    @app.get("/models/{model_name}")
    async def get_model(model_name: ModelName):
        if model_name is ModelName.alexnet:
            return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
        if model_name.value == "lenet":
            return {"model_name": model_name, "message": "LeCNN all the images"}
    
        return {"model_name": model_name, "message": "Have some residuals"}
    

```

Подсказка

Значение `"lenet"` также можно получить с помощью `ModelName.lenet.value`.

#### Возврат _элементов перечисления_

Из _операции пути_ можно вернуть _элементы перечисления_ , даже вложенные в тело JSON (например в `dict`).

Они будут преобразованы в соответствующие значения (в данном случае - строки) перед их возвратом клиенту:

Python 3.10+

```
 
    from enum import Enum
    
    from fastapi import FastAPI
    
    
    class ModelName(str, Enum):
        alexnet = "alexnet"
        resnet = "resnet"
        lenet = "lenet"
    
    
    app = FastAPI()
    
    
    @app.get("/models/{model_name}")
    async def get_model(model_name: ModelName):
        if model_name is ModelName.alexnet:
            return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
        if model_name.value == "lenet":
            return {"model_name": model_name, "message": "LeCNN all the images"}
    
        return {"model_name": model_name, "message": "Have some residuals"}
    

```

На стороне клиента вы получите такой JSON-ответ:

```
 
    {
      "model_name": "alexnet",
      "message": "Deep Learning FTW!"
    }
    

```

## Path-параметры, содержащие пути

Предположим, что есть _операция пути_ с путем `/files/{file_path}`.

Но вам нужно, чтобы `file_path` сам содержал _путь_ , например, `home/johndoe/myfile.txt`.

Тогда URL для этого файла будет такой: `/files/home/johndoe/myfile.txt`.

### Поддержка OpenAPI

OpenAPI не поддерживает способов объявления _параметра пути_ , содержащего внутри _путь_ , так как это может привести к сценариям, которые сложно определять и тестировать.

Тем не менее это можно сделать в **FastAPI** , используя один из внутренних инструментов Starlette.

Документация по-прежнему будет работать, хотя и не добавит никакой информации о том, что параметр должен содержать путь.

### Конвертер пути

Благодаря одной из опций Starlette, можете объявить _параметр пути_ , содержащий _путь_ , используя URL вроде:

```
 
    /files/{file_path:path}
    

```

В этом случае `file_path` \- это имя параметра, а часть `:path`, указывает, что параметр должен соответствовать любому _пути_.

Можете использовать так:

Python 3.10+

```
 
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/files/{file_path:path}")
    async def read_file(file_path: str):
        return {"file_path": file_path}
    

```

Подсказка

Возможно, вам понадобится, чтобы параметр содержал `/home/johndoe/myfile.txt` с ведущим слэшем (`/`).

В этом случае URL будет таким: `/files//home/johndoe/myfile.txt`, с двойным слэшем (`//`) между `files` и `home`.

## Резюме

Используя **FastAPI** вместе со стандартными объявлениями типов Python (короткими и интуитивно понятными), вы получаете:

  * Поддержку редактора кода (проверку ошибок, автозавершение и т.п.)
  * "Парсинг" данных
  * Валидацию данных
  * Аннотации API и автоматическую документацию

И объявлять типы достаточно один раз.

Это, вероятно, является главным заметным преимуществом **FastAPI** по сравнению с альтернативными фреймворками (кроме сырой производительности).
  *[`Enum`]: Enumeration - Перечисление
  *[сырой]: не считая оптимизаций
