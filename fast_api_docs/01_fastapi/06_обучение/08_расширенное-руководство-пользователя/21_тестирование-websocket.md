---
title: Тестирование WebSocket
source: https://fastapi.tiangolo.com/ru/advanced/testing-websockets/
---

# Тестирование WebSocket

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/advanced/testing-websockets/)

Вы можете использовать тот же `TestClient` для тестирования WebSocket.

Для этого используйте `TestClient` с менеджером контекста `with`, подключаясь к WebSocket:

Python 3.10+

```
 
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    from fastapi.websockets import WebSocket
    
    app = FastAPI()
    
    
    @app.get("/")
    async def read_main():
        return {"msg": "Hello World"}
    
    
    @app.websocket("/ws")
    async def websocket(websocket: WebSocket):
        await websocket.accept()
        await websocket.send_json({"msg": "Hello WebSocket"})
        await websocket.close()
    
    
    def test_read_main():
        client = TestClient(app)
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}
    
    
    def test_websocket():
        client = TestClient(app)
        with client.websocket_connect("/ws") as websocket:
            data = websocket.receive_json()
            assert data == {"msg": "Hello WebSocket"}
    

```

Примечание

Подробности смотрите в документации Starlette по [тестированию WebSocket](https://www.starlette.dev/testclient/#testing-websocket-sessions).
