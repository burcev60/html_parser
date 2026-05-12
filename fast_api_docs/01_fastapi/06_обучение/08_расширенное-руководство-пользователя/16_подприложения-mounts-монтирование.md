---
title: Подприложения — Mounts (монтирование)
source: https://fastapi.tiangolo.com/ru/advanced/sub-applications/
---

# Подприложения — Mounts (монтирование)

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/advanced/sub-applications/)

Если вам нужны два независимых приложения FastAPI, каждое со своим собственным OpenAPI и собственными интерфейсами документации, вы можете иметь основное приложение и «смонтировать» одно (или несколько) подприложений.

## Монтирование приложения **FastAPI**

«Монтирование» означает добавление полностью независимого приложения по конкретному пути; далее оно будет обрабатывать всё под этим путём, используя объявленные в подприложении _операции пути_.

### Приложение верхнего уровня

Сначала создайте основное, верхнего уровня, приложение **FastAPI** и его _операции пути_ :

Python 3.10+

```
 
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/app")
    def read_main():
        return {"message": "Hello World from main app"}
    
    
    subapi = FastAPI()
    
    
    @subapi.get("/sub")
    def read_sub():
        return {"message": "Hello World from sub API"}
    
    
    app.mount("/subapi", subapi)
    

```

### Подприложение

Затем создайте подприложение и его _операции пути_.

Это подприложение — обычное стандартное приложение FastAPI, но именно оно будет «смонтировано»:

Python 3.10+

```
 
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/app")
    def read_main():
        return {"message": "Hello World from main app"}
    
    
    subapi = FastAPI()
    
    
    @subapi.get("/sub")
    def read_sub():
        return {"message": "Hello World from sub API"}
    
    
    app.mount("/subapi", subapi)
    

```

### Смонтируйте подприложение

В вашем приложении верхнего уровня, `app`, смонтируйте подприложение `subapi`.

В этом случае оно будет смонтировано по пути `/subapi`:

Python 3.10+

```
 
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/app")
    def read_main():
        return {"message": "Hello World from main app"}
    
    
    subapi = FastAPI()
    
    
    @subapi.get("/sub")
    def read_sub():
        return {"message": "Hello World from sub API"}
    
    
    app.mount("/subapi", subapi)
    

```

### Проверьте автоматическую документацию API

Теперь запустите команду `fastapi`:

```
 
    $ fastapi dev
    
    <span style="color: green;">INFO</span>:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    

```

И откройте документацию по адресу <http://127.0.0.1:8000/docs>.

Вы увидите автоматическую документацию API для основного приложения, включающую только его собственные _операции пути_ :

![](https://fastapi.tiangolo.com/img/tutorial/sub-applications/image01.png)

Затем откройте документацию для подприложения по адресу <http://127.0.0.1:8000/subapi/docs>.

Вы увидите автоматическую документацию API для подприложения, включающую только его собственные _операции пути_ , все под корректным префиксом подпути `/subapi`:

![](https://fastapi.tiangolo.com/img/tutorial/sub-applications/image02.png)

Если вы попробуете взаимодействовать с любым из двух интерфейсов, всё будет работать корректно, потому что браузер сможет обращаться к каждому конкретному приложению и подприложению.

### Технические подробности: `root_path`

Когда вы монтируете подприложение, как описано выше, FastAPI позаботится о передаче пути монтирования для подприложения, используя механизм из спецификации ASGI под названием `root_path`.

Таким образом подприложение будет знать, что для интерфейса документации нужно использовать этот префикс пути.

У подприложения также могут быть свои собственные смонтированные подприложения, и всё будет работать корректно, потому что FastAPI автоматически обрабатывает все эти `root_path`.

Вы узнаете больше о `root_path` и о том, как использовать его явно, в разделе [За прокси](https://fastapi.tiangolo.com/ru/advanced/behind-a-proxy/) ([local](./17_за-прокси-сервером.md)).
