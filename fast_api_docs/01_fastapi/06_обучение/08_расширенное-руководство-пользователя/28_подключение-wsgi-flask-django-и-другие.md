---
title: Подключение WSGI — Flask, Django и другие
source: https://fastapi.tiangolo.com/ru/advanced/wsgi/
---

# Подключение WSGI — Flask, Django и другие

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/advanced/wsgi/)

Вы можете монтировать WSGI‑приложения, как вы видели в [Подприложения — Mounts](https://fastapi.tiangolo.com/ru/advanced/sub-applications/) ([local](./16_подприложения-mounts-монтирование.md)), [За прокси‑сервером](https://fastapi.tiangolo.com/ru/advanced/behind-a-proxy/) ([local](./17_за-прокси-сервером.md)).

Для этого вы можете использовать `WSGIMiddleware` и обернуть им ваше WSGI‑приложение, например Flask, Django и т.д.

## Использование `WSGIMiddleware`

Информация

Для этого требуется установить `a2wsgi`, например с помощью `pip install a2wsgi`.

Нужно импортировать `WSGIMiddleware` из `a2wsgi`.

Затем оберните WSGI‑приложение (например, Flask) в middleware (Промежуточный слой).

После этого смонтируйте его на путь.

Python 3.10+

```
 
    from a2wsgi import WSGIMiddleware
    from fastapi import FastAPI
    from flask import Flask, request
    from markupsafe import escape
    
    flask_app = Flask(__name__)
    
    
    @flask_app.route("/")
    def flask_main():
        name = request.args.get("name", "World")
        return f"Hello, {escape(name)} from Flask!"
    
    
    app = FastAPI()
    
    
    @app.get("/v2")
    def read_main():
        return {"message": "Hello World"}
    
    
    app.mount("/v1", WSGIMiddleware(flask_app))
    

```

Примечание

Ранее рекомендовалось использовать `WSGIMiddleware` из `fastapi.middleware.wsgi`, но теперь он помечен как устаревший.

Вместо него рекомендуется использовать пакет `a2wsgi`. Использование остаётся таким же.

Просто убедитесь, что пакет `a2wsgi` установлен, и импортируйте `WSGIMiddleware` из `a2wsgi`.

## Проверьте

Теперь каждый HTTP‑запрос по пути `/v1/` будет обрабатываться приложением Flask.

А всё остальное будет обрабатываться **FastAPI**.

Если вы запустите это и перейдёте по <http://localhost:8000/v1/>, вы увидите HTTP‑ответ от Flask:

```
 
    Hello, World from Flask!
    

```

А если вы перейдёте по <http://localhost:8000/v2>, вы увидите HTTP‑ответ от FastAPI:

```
 
    {
        "message": "Hello World"
    }
    

```
