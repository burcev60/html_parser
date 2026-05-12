---
title: Тестирование событий: lifespan и startup - shutdown
source: https://fastapi.tiangolo.com/ru/advanced/testing-events/
---

# Тестирование событий: lifespan и startup - shutdown

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/advanced/testing-events/)

Если вам нужно, чтобы `lifespan` выполнялся в ваших тестах, вы можете использовать `TestClient` вместе с оператором `with`:

Python 3.10+

```
 
    from contextlib import asynccontextmanager
    
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    
    items = {}
    
    
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        items["foo"] = {"name": "Fighters"}
        items["bar"] = {"name": "Tenders"}
        yield
        # clean up items
        items.clear()
    
    
    app = FastAPI(lifespan=lifespan)
    
    
    @app.get("/items/{item_id}")
    async def read_items(item_id: str):
        return items[item_id]
    
    
    def test_read_items():
        # Before the lifespan starts, "items" is still empty
        assert items == {}
    
        with TestClient(app) as client:
            # Inside the "with TestClient" block, the lifespan starts and items added
            assert items == {"foo": {"name": "Fighters"}, "bar": {"name": "Tenders"}}
    
            response = client.get("/items/foo")
            assert response.status_code == 200
            assert response.json() == {"name": "Fighters"}
    
            # After the requests is done, the items are still there
            assert items == {"foo": {"name": "Fighters"}, "bar": {"name": "Tenders"}}
    
        # The end of the "with TestClient" block simulates terminating the app, so
        # the lifespan ends and items are cleaned up
        assert items == {}
    

```

Вы можете узнать больше подробностей в статье [Запуск lifespan в тестах на официальном сайте документации Starlette.](https://www.starlette.dev/lifespan/#running-lifespan-in-tests)

Для устаревших событий `startup` и `shutdown` вы можете использовать `TestClient` следующим образом:

Python 3.10+

```
 
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    
    app = FastAPI()
    
    items = {}
    
    
    @app.on_event("startup")
    async def startup_event():
        items["foo"] = {"name": "Fighters"}
        items["bar"] = {"name": "Tenders"}
    
    
    @app.get("/items/{item_id}")
    async def read_items(item_id: str):
        return items[item_id]
    
    
    def test_read_items():
        with TestClient(app) as client:
            response = client.get("/items/foo")
            assert response.status_code == 200
            assert response.json() == {"name": "Fighters"}
    

```
